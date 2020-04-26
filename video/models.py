from django.conf import settings
from django.db import models

class Video(models.Model):

    class Category(models.TextChoices):
        Music = 'music'
        Movie = 'movie'
        Drama = 'drama'
        Comedy = 'comedy'
        Information = 'info'
        Daily = 'daily'
        Beauty = 'beauty'
        Art = 'art'
        Book = 'book'
        Sport = 'sport'
        Food = 'food'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_key = models.CharField(max_length=12)
    likes_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes_user')
    upload_date = models.DateTimeField(auto_now_add=True, null=True) # first created date
    category = models.TextField(choices=Category.choices, blank=True)

    class Meta:
        ordering = ['-upload_date']

    def count_likes_user(self):
        return self.likes_user.count()

    def __str__(self):
        return self.title
