from django.core.mail import send_mail

from django.conf import settings


def send_task_assignment_email(
    recipient_email,
    task_title
):

    subject = 'New Task Assigned'

    message = f'''
Hello,

You have been assigned a new task.

Task: {task_title}

Please login to Task Manager App.

Thank you.
'''

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
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
Hello,

You have been invited to join the team "{team_name}".

Click below to join the team:

{invite_link}

Thank you.
'''

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )