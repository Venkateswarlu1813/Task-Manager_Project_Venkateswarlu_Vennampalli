from django.urls import path

from .views import (
    TeamCreateListView,
    AddTeamMemberView,
    InviteTeamMemberView
)

urlpatterns = [

    path(
        '',
        TeamCreateListView.as_view(),
        name='teams'
    ),

    path(
        'add-member/',
        AddTeamMemberView.as_view(),
        name='add-member'
    ),

    path(
        'invite/',
        InviteTeamMemberView.as_view(),
        name='invite-team-member'
    ),
]