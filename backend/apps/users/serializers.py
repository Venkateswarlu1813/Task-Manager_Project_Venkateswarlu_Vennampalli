from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = (
            'id',
            'email',
            'username',
            'role',
            'is_active',
            'can_create_tasks',
            'created_at',
        )