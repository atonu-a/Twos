# views.py - Django Views

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as user_login ,logout as user_logout
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url="login")
def index(request):
    today = timezone.now().date()
    

    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    

    total_active_tasks = tasks.filter(is_completed=False).count()
    total_priority_tasks = tasks.filter(priority="High").count()
    total_future_tasks = tasks.filter(due_date__gt=today).count()
    
    data = {
        'tasks': tasks,
        'total_active_tasks': total_active_tasks,
        'total_priority_tasks': total_priority_tasks,
        'total_future_tasks': total_future_tasks,
    }
    return render(request, 'index.html', data)


@login_required(login_url="login")
def add_task(request):
    if request.method == "POST":
        name = request.POST.get("task_name")
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")
        Task.objects.create(
            user=request.user,
            name=name, 
            priority=priority,
            due_date=due_date if due_date else None
        )
        messages.info(request, "Mission Initiated!")
        
        MissionLog.objects.create(
            user = request.user,
            action = 'Initiated',
            task_name = name,
        )
        
        
    
    return redirect("index")

@login_required(login_url="login")
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    MissionLog.objects.create(
        user=request.user,
        action='Aborted',
        task_name=task.name
    )
    
    
    task.delete()
    messages.error(request, "Mission Aborted!")
    return redirect("index")

@login_required(login_url="login")
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    
    
    action_type = 'Accomplished' if task.is_completed else 'Reopened'
    if action_type=='Accomplished':
        messages.success(request, "Mission Accomplished")
    else:
        messages.info(request, "Mission Reopened")
    
    MissionLog.objects.create(
        user=request.user,
        action=action_type,
        task_name=task.name
    )
    return redirect("index")
    
def about(request):
    return render(request, "about.html")


@login_required(login_url="login")
def profile(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    tasks = Task.objects.order_by("-created_at")
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True)
    total_completed_tasks = completed_tasks.count()
    if total_tasks > 0 :
        success_rate = int((total_completed_tasks/total_tasks) * 100)
        
    else:
        success_rate = 0
    recent = MissionLog.objects.filter(user=request.user).order_by("-created_at")[:5]
    data = {
        'profile' : profile,
        'total_tasks' : total_tasks,
        'recent' : recent,
        'total_completed_tasks' : total_completed_tasks,
        'success_rate' : success_rate,
    }
    return render(request, "profile.html", data)


# Login registration system
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            messages.success(request,"Welcome Back Commander!🥳")
            return redirect("index")
    else:
        form = AuthenticationForm()
    data = {
        "form":form
    }

    return render(request,"login.html",data)

def logout(request):
    if request.method == "POST":
        user_logout(request)
        return redirect("login")
    return redirect("index")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.get_or_create(user=user)
            user_login(request, user)
            messages.success(request,"Welcome Commander!🎆")
            return redirect("edit")
        else:

            print(form.errors) 
    else:
        form = UserCreationForm()
        

    return render(request, "registration.html", {'form': form})
@login_required(login_url="login")
def edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        print(request.POST)
        profile.full_name = request.POST.get("full_name", profile.full_name)
        profile.bio = request.POST.get("bio", "")
        profile.location = request.POST.get("location", "")
        if request.FILES.get("profile_pic"):
            profile.profile_pic = request.FILES.get("profile_pic")

        
        profile.save()
        messages.success(request,"Commander Profile Updated Successfully")
        return redirect("profile")
    return render(request, "edit_profile.html", {"profile":profile})

@login_required(login_url="login")
def activities(request):
    recent = MissionLog.objects.filter(user=request.user).order_by("-created_at")
    data = {
        'recent' : recent
    }
    return render(request, "activity.html", data)
