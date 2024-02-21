from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    profilePic = models.ImageField()
