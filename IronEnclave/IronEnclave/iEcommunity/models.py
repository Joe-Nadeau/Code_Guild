from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

# Create your models here.

class Comment (models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null = True, blank = True)
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(null = True, blank = False)

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(null = True, blank = False)
    comments = models.ManyToManyField(Comment)

class Forum(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)

