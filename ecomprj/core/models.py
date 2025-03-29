# Create your models here.
from django import forms
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.forms import UserCreationForm

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group, related_name="custom_user_set", blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissins_set", blank= True
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

