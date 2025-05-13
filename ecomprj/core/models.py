# Create your models here.
from django import forms
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.forms import UserCreationForm

class Subscription(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    consent = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class VolunteerInterest(models.Model):
    INTEREST_CHOICES = [
        ('1', '1: CLASSES'),
        ('2', '2: ESTEAM'),
        ('3','3: STEM LIKE ME'),
        ('4','4: EARLY STEM VILLAGE'),
        ('5','5: SERVICE MATTERS'),
        ('6', '6: SPARK SUMMER CAMP'),
        ('7', '7: RECOGNITION MATTERS'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=25,blank=True)
    discover = models.CharField(verbose_name='How did you heard about Class Matters?', max_length=20,blank=True)
    interest_area = models.CharField(verbose_name='What pillar are you interested in representing?',max_length=10, choices=INTEREST_CHOICES, default='1')
    additional_info = models.TextField(verbose_name='Anything else you\'d like us to know?',blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}\n {self.email}"

class Donation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.FloatField(verbose_name="Donation Amount", default=0)
    recurring = models.BooleanField(verbose_name="Make this a monthly donation.")
    quick_subscribe = models.BooleanField(verbose_name="I'd like to subscribe now and recieve monthly updates.")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name} - ${self.amount}"

