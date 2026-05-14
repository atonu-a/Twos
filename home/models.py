from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    PRIORITY_CHOICES = [
        ('Low', "Low"),
        ('Medium', "Medium"),
        ('High', "High")
    ]
    name = models.CharField(max_length=50)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Low")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    
    
    def __anarchy__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    
    joined_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_profile_pic(self):
        if self.profile_pic:
            return self.profile_pic.url
        
        name = self.full_name or self.user.username
        return f"https://ui-avatars.com/api/?name={name}&size=128&background=6366f1&color=fff"
    