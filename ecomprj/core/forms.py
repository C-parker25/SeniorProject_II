from django import forms
from .models import Subscription, VolunteerInterest, Donation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email', 'first_name', 'last_name', 'consent']

class VolunteerInterestForm(forms.ModelForm):
    class Meta:
        model = VolunteerInterest
        fields = ['first_name', 'last_name', 'email', 'phone', 'occupation', 'discover', 'interest_area','additional_info']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['first_name','last_name', 'email', 'amount', 'recurring', 'quick_subscribe']