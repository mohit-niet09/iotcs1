from django.core.mail import send_mail
from django.conf import settings

def send_email_util(sub, body, reclist):
    subject = sub
    body = body
    from_email = settings.EMAIL_HOST_USER
    recipient_list = reclist
    send_mail(subject, body, from_email, recipient_list)
