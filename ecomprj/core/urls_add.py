from django.urls import path
from core.pages import index
from core.views import register_view, login_view

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("Signup/", register_view, name="sign-up"),
    path("login/", login_view, name="login")
]