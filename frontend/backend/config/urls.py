from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(

    openapi.Info(

        title="Task Manager API",

        default_version='v1',

        description="Task Management SaaS Backend APIs",

        contact=openapi.Contact(
            email="admin@gmail.com"
        ),
    ),

    public=True,

    permission_classes=(
        permissions.AllowAny,
    ),
)


def home(request):

    return HttpResponse("""

        <h1 style='font-family:Arial;
                   text-align:center;
                   margin-top:100px;
                   color:#2c3e50;'>

                Task Manager Backend Running Successfully

        </h1>

    """)


urlpatterns = [

    path('', home),

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/auth/',
        include('apps.authentication.urls')
    ),

    path(
        'api/users/',
        include('apps.users.urls')
    ),

    path(
        'api/tasks/',
        include('apps.tasks.urls')
    ),

    path(
        'api/teams/',
        include('apps.teams.urls')
    ),

    path(
        'api/notifications/',
        include('apps.notifications.urls')
    ),

    path(
        'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)