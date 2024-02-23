from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    register_time = models.IntegerField()
    session_hash = models.CharField(max_length=255, unique=True, default="")
