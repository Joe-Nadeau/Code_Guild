from django.contrib import admin

from . import models

admin.site.register(models.author)
admin.site.register(models.Book)



