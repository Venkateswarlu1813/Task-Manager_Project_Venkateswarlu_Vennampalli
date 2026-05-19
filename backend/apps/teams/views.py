from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import uuid

from .models import (
    Team,
    TeamMember,
    TeamInvitation
)

from .serializers import (
    TeamSerializer,
    TeamMemberSerializer,
    TeamInvitationSerializer
)

from apps.common.email_service import (
    send_team_invitation_email
)


class TeamCreateListView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):

        teams = Team.objects.filter(
            created_by=request.user
        ).order_by('-created_at')

        serializer = TeamSerializer(
            teams,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = TeamSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(
                created_by=request.user
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AddTeamMemberView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = TeamMemberSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                'message': 'Member added successfully'
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class InviteTeamMemberView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, request):

        team_id = request.data.get('team')

        invited_email = request.data.get(
            'invited_email'
        )

        if not team_id or not invited_email:

            return Response({
                'error': 'team and invited_email are required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:

            team = Team.objects.get(id=team_id)

        except Team.DoesNotExist:

            return Response({
                'error': 'Team not found'
            }, status=status.HTTP_404_NOT_FOUND)

        token = str(uuid.uuid4())

        invitation = TeamInvitation.objects.create(

            team=team,

            invited_by=request.user,

            invited_email=invited_email,

            token=token
        )

        send_team_invitation_email(

            recipient_email=invited_email,

            team_name=team.team_name,

            token=token
        )

        serializer = TeamInvitationSerializer(
            invitation
        )

        return Response({

            'message': 'Invitation sent successfully',

            'invitation': serializer.data
        })