from django.urls import path

from .views import (
    CurrentUserView,
    UserListView,
    ToggleUserActiveView,
    ToggleTaskPermissionView
)

urlpatterns = [

    path(
        '',
        UserListView.as_view(),
        name='user-list'
    ),

    path(
        '<int:user_id>/toggle-active/',
        ToggleUserActiveView.as_view(),
        name='toggle-user-active'
    ),

    path(
        '<int:user_id>/toggle-task-permission/',
        ToggleTaskPermissionView.as_view(),
        name='toggle-task-permission'
    ),

    path(
    'me/',
    CurrentUserView.as_view()
    ),
]