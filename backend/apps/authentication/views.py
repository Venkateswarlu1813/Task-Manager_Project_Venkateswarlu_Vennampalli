from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

from google.oauth2 import id_token

from google.auth.transport import requests

from .serializers import (
    RegisterSerializer,
    LoginSerializer
)

User = get_user_model()


class RegisterView(APIView):

    authentication_classes = []

    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({

                'message': 'User registered successfully'

            }, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):

    authentication_classes = []

    permission_classes = []

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

                'access': str(refresh.access_token),

                'refresh': str(refresh),

            }, status=status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class GoogleLoginView(APIView):

    authentication_classes = []

    permission_classes = []

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

            user = User.objects.filter(
                email=email
            ).first()

            if not user:

                user = User.objects.create_user(
                    email=email,
                    username=name,
                    password=None
                )

            refresh = RefreshToken.for_user(user)

            return Response({

                'message': 'Google login successful',

                'user': {

                    'id': user.id,

                    'email': user.email,

                    'username': user.username,

                    'role': user.role,
                },

                'access': str(refresh.access_token),

                'refresh': str(refresh),

            })

        except Exception as e:

            return Response({

                'error': str(e)

            }, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):

    authentication_classes = [
        JWTAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        user = request.user

        return Response({


        })