from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.conf import settings

User = settings.AUTH_USER_MODEL

def register_view(request):

    if request.method =="POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Congratulations {username}. Your account has been created succesfully.")
            new_user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
            

def index(request):
    return HttpResponse("welcome to my shop")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.all(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist.")

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in.")
                return redirect("core:index")
            else:
                messages.warning(request, "User does not exist, Create an account.")

        context = {


        }

        return redirect(request, "core/login.html", context)
        
