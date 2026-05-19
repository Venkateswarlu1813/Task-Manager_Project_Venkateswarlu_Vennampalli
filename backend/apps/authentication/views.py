from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import (RegisterSerializer,LoginSerializer)
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):

    authentication_classes = []

    permission_classes = []

    def post(self, request):

        username = request.data.get('username')

        email = request.data.get('email')

        password = request.data.get('password')

        if User.objects.filter(email=email).exists():

            return Response({
                'error': 'Email already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response({
            'message': 'User registered successfully',
            'user_id': user.id,
            'email': user.email
        }, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        if serializer.is_valid():

            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)

            return Response({

                'message': 'Login successful',

                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                    'role': user.role,
                },

                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }

            }, status=status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class GoogleLoginView(APIView):

    def post(self, request):

        token = request.data.get('token')

        if not token:

            return Response({
                'error': 'Google token required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:

            user_info = id_token.verify_oauth2_token(
                token,
                requests.Request()
            )

            email = user_info.get('email')

            name = user_info.get('name')

            google_id = user_info.get('sub')

            user = User.objects.filter(
                email=email
            ).first()

            if not user:

                user = User.objects.create(
                    email=email,
                    username=name,
                    google_id=google_id,
                    auth_provider='google'
                )

                user.set_unusable_password()

                user.save()

            refresh = RefreshToken.for_user(user)

            return Response({

                'message': 'Google login successful',

                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                    'role': user.role,
                },

                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }

            })

        except Exception as e:

            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        

class ProfileView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({

            'id': user.id,
            'email': user.email,
            'username': user.username,
            'role': user.role,
            'can_create_tasks': user.can_create_tasks,
            'auth_provider': user.auth_provider,

        })