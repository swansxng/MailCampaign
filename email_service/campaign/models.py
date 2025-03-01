from django.db import models

class EmailOpen(models.Model):
    email_recipient = models.TextField(max_length=255)
    email_id = models.TextField(unique=True, null=False)
    opened_at = models.DateTimeField(auto_now_add=True, null=True)