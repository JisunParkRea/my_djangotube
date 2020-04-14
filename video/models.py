from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_key = models.CharField(max_length=12)