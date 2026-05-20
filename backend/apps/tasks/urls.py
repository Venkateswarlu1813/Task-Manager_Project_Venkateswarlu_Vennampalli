from django.urls import path

from .views import (
    TaskView,
    TaskDetailView,
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
        TaskView.as_view(),
        name='tasks'
    ),

    path(
        '<int:pk>/',
        TaskDetailView.as_view(),
        name='task-detail'
    ),

    path(
        'assign/',
        AssignTaskView.as_view(),
        name='assign-task'
    ),

    path(
        'tasks/<int:task_id>/status/',
        UpdateTaskStatusView.as_view(),
        name='task-status'
    ),

    path(
        'stats/',
        DashboardStatsView.as_view(),
        name='dashboard-stats'
    ),

    path(
        'search/',
        TaskSearchFilterView.as_view(),
        name='task-search'
    ),

    path(
        'comments/<int:task_id>/',
        TaskCommentView.as_view(),
        name='task-comments'
    ),

    path(
        'attachments/<int:task_id>/',
        TaskAttachmentView.as_view(),
        name='task-attachments'
    ),

]