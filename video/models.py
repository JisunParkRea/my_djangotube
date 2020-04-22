from django.conf import settings
from django.db import models
from django.conf import settings

class Video(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_key = models.CharField(max_length=12)
    likes_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes_user')

    def count_likes_user(self):
        return self.likes_user.count()

    def __str__(self):
        return self.title
