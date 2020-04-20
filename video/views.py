from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm, UserForm, LoginForm

def video_list(request):
    video_list = Video.objects.all()
    return render(request, 'video/video_list.html', {'video_list':video_list})

@login_required
def video_new(request):
    if request.method == 'POST': # 새로운 비디오 데이터를 업로드할 때
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False) # 받은 데이터를 바로 Video모델에 저장하지 말기
            video.author = request.user # author 추가
            video.save() # 변경사항 저장
        return redirect('video_list')
    elif request.method == 'GET': # 새로운 비디오를 추가할 템플릿을 가져와야할 때
        return render(request, 'video/video_new.html')

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video/video_detail.html', {'video':video})

@login_required
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    return redirect('video_list')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('video_list')
    else:
        form = UserForm()
        return render(request, 'video/user_new.html')
        
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('video_list')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request, 'video/user_login.html')

def signout(request):
    logout(request)
    return redirect('video_list')
