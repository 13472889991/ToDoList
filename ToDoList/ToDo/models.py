from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at=datetime.now
    due = models.DateTimeField(default=datetime.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default= None)
    def __str__(self):
        return self.title
    
# Create your models here.
