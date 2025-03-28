from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder""Username"}))
    email = forms.EmailField(widget=forms.EmailField(attrs={"placeholder""Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder""Password"}))
    password12 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder""Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
