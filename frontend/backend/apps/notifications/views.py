from .models import ActivityLog
from apps.common.activity_service import (
    create_activity_log
)

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ActivityLog


class ActivityLogView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):

        logs = ActivityLog.objects.filter(
            user=request.user
        )

        data = []

        for log in logs:

            data.append({

                'action': log.action,

                'created_at': log.created_at
            })

        return Response(data)