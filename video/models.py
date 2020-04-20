from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_key = models.CharField(max_length=12)