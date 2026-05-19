from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    model = User

    list_display = (
        'id',
        'email',
        'username',
        'role',
        'is_active',
        'can_create_tasks',
        'created_at',
    )

    list_filter = (
        'role',
        'is_active',
        'auth_provider',
    )

    ordering = ('-created_at',)

    search_fields = (
        'email',
        'username',
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),

        ('Personal Info', {
            'fields': (
                'username',
            )
        }),

        ('Permissions', {
            'fields': (
                'role',
                'is_active',
                'is_staff',
                'is_superuser',
                'can_create_tasks',
                'groups',
                'user_permissions',
            )
        }),

        ('Authentication', {
            'fields': (
                'auth_provider',
                'google_id',
            )
        }),

        ('Important Dates', {
            'fields': (
                'last_login',
                'created_at',
                'updated_at',
            )
        }),
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'last_login',
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'role',
                'is_active',
                'is_staff',
            ),
        }),
    )