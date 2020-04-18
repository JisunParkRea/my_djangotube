from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('new/', views.video_new, name='video_new'),
    path('<int:pk>', views.video_detail, name='video_detail'),
    path('<int:pk>/delete', views.video_delete, name='video_delete'),
    path('signup/', views.signup, name='user_signup'),
    path('login/', views.signin, name='user_login'),
]