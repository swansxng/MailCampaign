import uuid
import time
from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import EmailOpen


@shared_task
def send_email_task(request, subject, message, email_list, delay):
    time.sleep(delay)
    for recipient in email_list:
        try:
            track_id = str(uuid.uuid4())
            html = render_to_string('mail_temp.html',
                                    {'request': request, "subject": subject, "data": message, "track_id": track_id})
            text_content = strip_tags(html)
            email = EmailMultiAlternatives(subject, text_content, 'mailto.fssocial@gmail.com', [recipient])
            email.attach_alternative(html, "text/html")
            email.send()
            print("creating db")
            try:
                EmailOpen.objects.create(email_recipient=recipient, email_id=track_id)
            except Exception as e:
                print(f"Error: {e}")
            print("created")
        except Exception:
            pass
