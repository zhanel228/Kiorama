from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.news_list, name='news_list'), 
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('add/', views.add_news, name='add_news'),
    path('reels/', views.video_list, name='reelse'), 
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='news/login.html')),
    path('profile/', views.profile_view, name='profile'), 
    path('like/<int:id>/', views.like_view, name='like_post'),
    path('reels/add/', views.add_video, name='add_video'),
]