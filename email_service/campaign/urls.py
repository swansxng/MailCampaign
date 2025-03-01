from django.urls import path
from .views import *

urlpatterns = [
    path('', email_form, name='email_form'),
    path('tracking/<str:track_id>', tracking, name='tracking'),
]