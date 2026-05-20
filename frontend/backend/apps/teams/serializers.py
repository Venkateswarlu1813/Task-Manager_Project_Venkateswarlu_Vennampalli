from rest_framework import serializers

from .models import Team, TeamMember
from .models import TeamInvitation

class TeamInvitationSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = TeamInvitation

        fields = '__all__'

        read_only_fields = (
            'invited_by',
            'token',
            'status'
        )
        
class TeamSerializer(serializers.ModelSerializer):

    created_by_email = serializers.CharField(
        source='created_by.email',
        read_only=True
    )

    class Meta:

        model = Team

        fields = (
            'id',
            'team_name',
            'description',
            'created_by',
            'created_by_email',
            'created_at',
        )

        read_only_fields = (
            'created_by',
        )


class TeamMemberSerializer(serializers.ModelSerializer):

    user_email = serializers.CharField(
        source='user.email',
        read_only=True
    )

    class Meta:

        model = TeamMember

        fields = (
            'id',
            'team',
            'user',
            'user_email',
            'joined_at',
        )