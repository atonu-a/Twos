# urls.py - Django URL Configuration

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name ='profile'),
    path('login/', views.login, name ='login'),
    path('register/', views.register, name ='register'),
    path('edit/', views.edit, name ='edit'),
    
    
]