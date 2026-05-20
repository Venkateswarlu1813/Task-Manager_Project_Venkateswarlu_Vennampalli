from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminUserRole


class UserListView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole
    ]

    def get(self, request):

        users = User.objects.all().order_by('-created_at')

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)


class ToggleUserActiveView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole
    ]

    def patch(self, request, user_id):

        try:

            user = User.objects.get(id=user_id)

        except User.DoesNotExist:

            return Response({
                'error': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)

        user.is_active = not user.is_active

        user.save()

        return Response({
            'message': 'User active status updated',
            'is_active': user.is_active
        })


class ToggleTaskPermissionView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole
    ]

    def patch(self, request, user_id):

        try:

            user = User.objects.get(id=user_id)

        except User.DoesNotExist:

            return Response({
                'error': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)

        user.can_create_tasks = (
            not user.can_create_tasks
        )

        user.save()

        return Response({
            'message': 'Task permission updated',
            'can_create_tasks': user.can_create_tasks
        })

class CurrentUserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "role": request.user.role,
        })