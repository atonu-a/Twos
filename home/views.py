# views.py - Django Views

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


def index(request):


    
    return render(request, 'index.html')

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
