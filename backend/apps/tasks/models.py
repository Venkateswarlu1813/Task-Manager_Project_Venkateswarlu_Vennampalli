from django.db import models

from apps.users.models import User
from apps.teams.models import Team


class Task(models.Model):

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    STATUS_CHOICES = (
        ('todo', 'Todo'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )

    due_date = models.DateTimeField(
        blank=True,
        null=True
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_tasks'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title

    class Meta:

        db_table = 'tasks'

class TaskAssignee(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='assignees'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True
    )
class TaskComment(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.email} - {self.task.title}"

    class Meta:

        db_table = 'task_comments'

        ordering = ['-created_at']

    def __str__(self):

        return f"{self.user.email} - {self.task.title}"

    class Meta:

        db_table = 'task_assignees'

        unique_together = ('task', 'user')
    class TaskComment(models.Model):

        task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.comment
    
class TaskAttachment(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='attachments'
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to='task_attachments/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.file.name