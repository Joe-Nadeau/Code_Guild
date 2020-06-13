from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

# Create your models here.

class Users(models.Model):
    pass

class Profiles(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null = True, blank = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_img = models.ImageField(upload_to='profile')
    bio = models.CharField(max_length=10000)
    weight_class = models.CharField(max_length=3)