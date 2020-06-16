from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Profiles)
admin.site.register(models.Users)