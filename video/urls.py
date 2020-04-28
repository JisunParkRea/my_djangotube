from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('new/', views.video_new, name='video_new'),
    path('<int:pk>/delete', views.video_delete, name='video_delete'),
    path('signup/', views.signup, name='user_signup'),
    path('login/', views.signin, name='user_login'),
    path('logout/', views.signout, name='user_logout'),
    path('like/', views.video_like, name='video_like'),
    path('myVideo/', views.my_video, name='my_video'),
    path('likeVideo/', views.like_video, name='like_video'),
    path('<str:category>/', views.video_category, name='video_category'),
]