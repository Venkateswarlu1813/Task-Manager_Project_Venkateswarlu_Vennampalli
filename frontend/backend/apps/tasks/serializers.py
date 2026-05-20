from rest_framework import serializers
from .models import TaskAttachment

from .models import (
    Task,
    TaskAssignee,
    TaskComment
)


class TaskSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Task

        fields = '__all__'

        read_only_fields = (
            'created_by',
        )


class TaskAssigneeSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = TaskAssignee

        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):

    user_email = serializers.EmailField(
        source='user.email',
        read_only=True
    )

    class Meta:
        model = TaskComment

        fields = [
            'id',
            'task',
            'user',
            'user_email',
            'comment',
            'created_at'
        ]

        read_only_fields = [
            'task',
            'user',
            'created_at'
        ]

class TaskAttachmentSerializer(serializers.ModelSerializer):

    uploaded_by = serializers.ReadOnlyField(
        source='uploaded_by.email'
    )

    class Meta:

        model = TaskAttachment

        fields = [
            'id',
            'task',
            'uploaded_by',
            'file',
            'uploaded_at'
        ]

        read_only_fields = [
            'task',
            'uploaded_by',
            'uploaded_at'
        ]