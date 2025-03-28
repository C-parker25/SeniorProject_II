from django.urls import path
from core.pages import index

app_name = "core"

urlpatterns = [
    path("",index, name = "index") # Default to homepage
]