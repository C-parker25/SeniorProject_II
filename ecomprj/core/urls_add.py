from django.urls import path
from core.pages import index
from django import views

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("Signup/", views.register_view, name="sign-up"),
    path("login/", views.login_view, name="login")
]