from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank = True)
    last_name = models.CharField(max_length=30, blank = True)
    age = models.CharField(max_length=3, blank = True)
    profile_img = models.ImageField(blank = True)
    bio = models.CharField(max_length=10000, blank = True)

    gender_choice = [
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Non-Binary"),
        ("T", "Transgender"),
    ]

    gender = models.CharField(choices = gender_choice, max_length=12)

    # Weight gathered from USAPL National qualifying totals https://www.usapowerlifting.com/lifters-corner/qualifying-totals/
    
    weight_class_choices = [
        ("43 kg", "94 lb"),
        ("47 kg", "103 lb"),
        ("52 kg", "114 lb"),
        ("53 kg", "116 lb"),
        ("57 kg", "125 lb"),
        ("59 kg", "130 lb"),
        ("63 kg", "138 lb"),
        ("66 kg", "145 lb"),
        ("72 kg", "158 lb"),
        ("74 kg", "163 lb"),
        ("83 kg", "182 lb"),
        ("84 kg", "185 lb"),
        ("84 kg+", "185 lb+"),
        ("93 kg", "205 lb"),
        ("105", "231 lb"),
        ("120", "264 lb"),
        ("120 kg+", "264 lb+"),
    ]

    weight_class = models.CharField(choices = weight_class_choices, max_length=7)



