from django.db import models

from apps.users.models import User


class Team(models.Model):

    team_name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_teams'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.team_name

    class Meta:

        db_table = 'teams'

class TeamMember(models.Model):

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='members'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.email} - {self.team.team_name}"

    class Meta:

        db_table = 'team_members'

        unique_together = ('team', 'user')

class TeamInvitation(models.Model):

    STATUS_CHOICES = (

        ('pending', 'Pending'),

        ('accepted', 'Accepted'),
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    invited_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_invitations'
    )

    invited_email = models.EmailField()

    token = models.CharField(
        max_length=255,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.invited_email