from django.db import models

from apps.users.models import User


class ActivityLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    action = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.email} - {self.action}"

    class Meta:

        db_table = 'activity_logs'

        ordering = ['-created_at']