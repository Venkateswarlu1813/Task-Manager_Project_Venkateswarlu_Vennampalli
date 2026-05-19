from apps.notifications.models import ActivityLog


def create_activity_log(
    user,
    action
):

    ActivityLog.objects.create(
        user=user,
        action=action
    )
    
def send_team_invitation_email(
    recipient_email,
    team_name,
    token
):

    subject = f'Invitation to join {team_name}'

    invite_link = (
        f'http://localhost:3000/join-team/{token}'
    )

    message = f'''
You have been invited to join the team "{team_name}".

Click below to join:

{invite_link}
'''

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )