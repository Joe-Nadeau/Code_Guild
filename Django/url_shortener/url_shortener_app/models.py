from django.db import models

# Create your models here.

class Model_U(models.Model):
    url = models.CharField(max_length = 200)
    url_hash = models.CharField(max_length = 200)