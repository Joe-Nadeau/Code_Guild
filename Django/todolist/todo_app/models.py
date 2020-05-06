from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class TodoItem(models.Model):
    task_description = models.TextField(blank = False, null = True)
    created_date = models.DateTimeField(default = timezone.now)
    completion_date = models.DateTimeField(blank = True, null = True)
    is_completed = models.BooleanField(default = False)
    

    def complete_task(self):
        self.is_completed = True
        self.completion_date = timezone.now()
        return self.is_completed

    def update(self):
        self.task_description