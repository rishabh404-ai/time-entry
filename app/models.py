from django.db import models
from django.contrib.auth.models import User

PROJECT_CHOICES =( 
        ("1", "Web Development"), 
        ("2", "Software Development"), 
        ("3", "Machine Learning"), 
        ("4", "Deep Learning"), 
        ("5", "Natural Language Processing"), 
    ) 

class LogEntry(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='users')
    task = models.CharField(max_length=1000)
    project = models.CharField(max_length=1, choices=PROJECT_CHOICES)
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
    duration = models.DurationField(null=True,blank=True)

    def __str__(self):
        return self.task