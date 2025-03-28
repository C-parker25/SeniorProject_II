# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.forms import UserCreationForm



class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_Length=100)
    bio = models.CharField(max_Length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

