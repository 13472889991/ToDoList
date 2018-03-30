from django.db import models
from datetime import datetime
class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at=datetime.now
    due = models.DateTimeField()
    def __str__(self):
        return self.title
    
# Create your models here.
