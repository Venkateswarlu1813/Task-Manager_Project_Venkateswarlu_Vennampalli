from django.contrib import admin

from .models import (
    Task,
    TaskAssignee,
    TaskComment
)

admin.site.register(Task)
admin.site.register(TaskAssignee)
admin.site.register(TaskComment)