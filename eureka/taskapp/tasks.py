"""Celery tasks."""

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from eureka.users.models import User
from eureka.jobs.models import Job

# Celery
from celery.decorators import task, periodic_task

# Utilities
import jwt
import time
from datetime import timedelta


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.email,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = 'Welcome @{}! Verifica tu cuenta para acceder a Eureka Jobs'.format(user.email)
    from_email = 'Eureka Jobs <noreply@eurekajobs.com>'
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token': verification_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()


@periodic_task(name='disable_finished_jobs', run_every=timedelta(days=1))
def disable_finished_jobs():
    """Disable finished jobs."""
    now = timezone.now()
    offset = now + timedelta(minutes=20)

    # Update jobs that have already finished
    jobs = Job.objects.filter(
        finished_at__lte=now,
        is_active=True
    )
    jobs.update(is_active=False)
