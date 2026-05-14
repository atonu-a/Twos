# views.py - Django Views

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as user_login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    today = timezone.now().date()
    
    tasks = Task.objects.order_by("-created_at")
    completed_tasks = tasks.filter(is_completed=False)
    total_completed_tasks = completed_tasks.count();
    high_priority_tasks = tasks.filter(priority="High")
    total_priority_tasks = high_priority_tasks.count()
    future_tasks = tasks.filter(due_date__gt=today)
    total_future_tasks = future_tasks.count()
    
    data = {
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        'total_completed_tasks' : total_completed_tasks,
        'high_priority_tasks': high_priority_tasks,
        'total_priority_tasks' : total_priority_tasks,
        'future_tasks':future_tasks,
        'total_future_tasks' : total_future_tasks,
        
    }
    return render(request, 'index.html', data)


def add_task(request):
    if request.method == "POST":
        name = request.POST.get("task_name")
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")
        Task.objects.create(
            name=name, 
            priority=priority,
            due_date=due_date if due_date else None
            )
    
    return redirect("index")

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("index")


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("index")
    
def about(request):
    return render(request, "about.html")

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    data = {
        'profile':profile
    }
    return render(request, "profile.html", data)

def login(request):
    return render(request,"login.html")




# Login registration system

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.get_or_create(user=user)
            user_login(request, user)
            return redirect("edit")
        else:

            print(form.errors) 
    else:
        form = UserCreationForm()
    
    return render(request, "registration.html", {'form': form})

def edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        print(request.POST)
        profile.full_name = request.POST.get("full_name", "")
        profile.bio = request.POST.get("bio", "")
        profile.location = request.POST.get("location", "")

        
        profile.save()
        return redirect("profile")
    return render(request, "edit_profile.html", {"profile":profile})