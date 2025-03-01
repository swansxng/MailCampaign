import uuid
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.timezone import now

from .models import EmailOpen
from .tasks import send_email_task
# Create your views here.

def email_form(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_list = request.POST.get('emails').split()
        delay = request.POST.get('delay')
        try:
            delay = int(delay)
        except ValueError:
            delay = 0

        if delay != 0:
            send_email_task(request, subject, message, email_list, delay)
        else:
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

        return JsonResponse({'status': 'success'})

    return render(request, "email_form.html")

def tracking(request, track_id):
    print("ping")
    EmailOpen.objects.filter(email_id=track_id).update(opened_at=now())
    print("ping_1")
    pixel = b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b"
    return HttpResponse(pixel, content_type="image/gif")