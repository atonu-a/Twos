from django.db import models

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