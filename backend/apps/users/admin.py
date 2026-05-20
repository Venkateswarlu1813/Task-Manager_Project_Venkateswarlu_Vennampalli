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
        'is_staff',
        'is_active',
    )

    search_fields = (
        'email',
        'username',
    )

    ordering = (
        'id',
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        ('Personal Info', {
            'fields': ('username',)
        }),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )

    filter_horizontal = (
        'groups',
        'user_permissions',
    )