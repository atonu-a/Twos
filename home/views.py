# views.py - Django Views

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .models import *


def index(request):
    tasks = Task.objects.order_by("-created_at")
    
    data = {
        'tasks':tasks,
    }
    return render(request, 'index.html', data)


def add_task(request):
    if request.method == "POST":
        name = request.POST.get("task_name")
        priority = request.POST.get("priority")
        Task.objects.create(name=name, priority=priority)
    
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

def profile(request):
    return render(request, "profile.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"registration.html")


def edit(request):
    return render(request,"edit_profile.html")
