from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import cloudinary.uploader

from .models import (
    Task,
    TaskAssignee,
    TaskComment,
    TaskAttachment
)

from .serializers import (
    TaskSerializer,
    TaskAssigneeSerializer,
    TaskCommentSerializer,
    TaskAttachmentSerializer
)

from apps.users.models import User
from apps.teams.models import Team

from apps.common.email_service import (
    send_task_assignment_email
)

from apps.common.activity_service import (
    create_activity_log
)


class TaskView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        tasks = Task.objects.filter(
            created_by=request.user
        )

        data = []

        for task in tasks:

            data.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "status": task.status,
                "due_date": task.due_date,
            })

        return Response(data)

    def post(self, request):

        try:

            title = request.data.get("title")

            description = request.data.get("description")

            priority = request.data.get("priority")

            due_date = request.data.get("due_date")

            team = Team.objects.first()

            if not team:

                return Response(
                    {
                        "error": "Create team first in Django admin"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            task = Task.objects.create(

                title=title,

                description=description,

                priority=priority,

                due_date=due_date,

                team=team,

                created_by=request.user,
            )

            return Response(
                {
                    "message": "Task created successfully",
                    "task_id": task.id
                },
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

class AssignTaskView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = TaskAssigneeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            assignment = serializer.save()

            create_activity_log(
                user=request.user,
                action=f"Assigned task '{assignment.task.title}' to {assignment.user.email}"
            )

            send_task_assignment_email(
                recipient_email=assignment.user.email,
                task_title=assignment.task.title
            )

            return Response({
                'message': 'Task assigned successfully'
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UpdateTaskStatusView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, task_id):

        try:

            task = Task.objects.get(id=task_id)

        except Task.DoesNotExist:

            return Response(
                {
                    'error': 'Task not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        status_value = request.data.get('status')

        if status_value not in [
            'todo',
            'in_progress',
            'completed'
        ]:

            return Response(
                {
                    'error': 'Invalid status'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        task.status = status_value

        task.save()

        create_activity_log(
            user=request.user,
            action=f"Updated task '{task.title}' status to {task.status}"
        )

        return Response({
            'message': 'Task status updated',
            'status': task.status
        })


class DashboardStatsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        tasks = Task.objects.filter(
            created_by=request.user
        )

        total_tasks = tasks.count()

        completed_tasks = tasks.filter(
            status='completed'
        ).count()

        pending_tasks = tasks.filter(
            status='todo'
        ).count()

        in_progress_tasks = tasks.filter(
            status='in_progress'
        ).count()

        high_priority_tasks = tasks.filter(
            priority='high'
        ).count()

        return Response({

            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'in_progress_tasks': in_progress_tasks,
            'high_priority_tasks': high_priority_tasks,

        })


class TaskSearchFilterView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        tasks = Task.objects.filter(
            created_by=request.user
        )

        search = request.GET.get('search')

        status_filter = request.GET.get('status')

        priority_filter = request.GET.get('priority')

        if search:

            tasks = tasks.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        if status_filter:

            tasks = tasks.filter(
                status=status_filter
            )

        if priority_filter:

            tasks = tasks.filter(
                priority=priority_filter
            )

        serializer = TaskSerializer(
            tasks,
            many=True
        )

        return Response(serializer.data)


class TaskCommentView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):

        comments = TaskComment.objects.filter(
            task_id=task_id
        )

        serializer = TaskCommentSerializer(
            comments,
            many=True
        )

        return Response(serializer.data)

    def post(self, request, task_id):

        serializer = TaskCommentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(
                user=request.user,
                task_id=task_id
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TaskAttachmentView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):

        try:

            task = Task.objects.get(id=task_id)

        except Task.DoesNotExist:

            return Response(
                {
                    'error': 'Task not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        uploaded_file = request.FILES.get('file')

        if not uploaded_file:

            return Response(
                {
                    'error': 'File required'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        upload_result = cloudinary.uploader.upload(
            uploaded_file,
            resource_type='auto'
        )

        attachment = TaskAttachment.objects.create(
            task=task,
            uploaded_by=request.user,
            file=upload_result['secure_url']
        )

        serializer = TaskAttachmentSerializer(
            attachment
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    
class TaskDetailView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):

        try:

            task = Task.objects.get(
                id=pk,
                created_by=request.user
            )

            task.title = request.data.get(
                "title",
                task.title
            )

            task.description = request.data.get(
                "description",
                task.description
            )

            task.priority = request.data.get(
                "priority",
                task.priority
            )

            task.status = request.data.get(
                "status",
                task.status
            )

            task.due_date = request.data.get(
                "due_date",
                 task.due_date
)

            task.save()

            return Response({
                "message": "Task updated successfully"
            })

        except Task.DoesNotExist:

            return Response(
                {
                    "error": "Task not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):

        try:

            task = Task.objects.get(
                id=pk,
                created_by=request.user
            )

            task.delete()

            return Response({
                "message": "Task deleted successfully"
            })

        except Task.DoesNotExist:

            return Response(
                {
                    "error": "Task not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )