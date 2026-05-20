from rest_framework import serializers

from django.contrib.auth import authenticate

from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password'
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField()

    def validate(self, data):

        email = data.get('email')

        password = data.get('password')

        try:

            user = User.objects.get(
                email=email
            )

        except User.DoesNotExist:

            raise serializers.ValidationError(
                "Invalid credentials"
            )

        if not user.check_password(password):

            raise serializers.ValidationError(
                "Invalid credentials"
            )

        data['user'] = user

        return data