from django import forms
from .models import Video
from django.contrib.auth.models import User

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'video_key']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']