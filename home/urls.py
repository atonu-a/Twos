# urls.py - Django URL Configuration

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name ='profile'),
    path('login/', views.login, name ='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name ='register'),
    path('edit/', views.edit, name ='edit'),
    path("add_task/", views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("activities/", views.activities, name="activities")
    
    
]