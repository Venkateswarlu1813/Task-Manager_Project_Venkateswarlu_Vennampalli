from django.urls import path

from .views import (
    TaskCreateListView,
    AssignTaskView,
    UpdateTaskStatusView,
    DashboardStatsView,
    TaskSearchFilterView,
    TaskCommentView,
    TaskAttachmentView
)
urlpatterns = [

    path(
        '',
        TaskCreateListView.as_view(),
        name='task-list-create'
    ),

    path(
        'assign/',
        AssignTaskView.as_view(),
        name='assign-task'
    ),

    path(
        '<int:task_id>/update-status/',
        UpdateTaskStatusView.as_view(),
        name='update-task-status'
    ),

    path(
        'dashboard/',
        DashboardStatsView.as_view(),
        name='dashboard-stats'
    ),

    path(
        'search-filter/',
        TaskSearchFilterView.as_view(),
        name='task-search-filter'
    ),

    path(
    '<int:task_id>/comments/',
    TaskCommentView.as_view(),
    name='task-comments'
    ),

    path(
    '<int:task_id>/attachments/',
    TaskAttachmentView.as_view()
    ),
]