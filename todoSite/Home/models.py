from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=10000)
    deadline = models.CharField(max_length=255)
    user_hash = models.CharField(max_length=255, default="")


