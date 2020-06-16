from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

# Create your models here.

class graph(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null = True, blank = True)
    weight = models.IntegerField()

    lift_choices = [
        ("SQ", "Squat"),
        ("B", "Bench"),
        ("D", "Deadlift"),
        ("P", "Press"),
    ]

    lift = models.CharField(choices = lift_choices, max_length=8)


