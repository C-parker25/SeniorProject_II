from django.urls import path
from core.pages import index
from core.views import shop_view, cart_view, getinvolved_view, donate_view, subscribe_view, volunteer_view, community_view

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("getinvolved/", getinvolved_view, name="getinvolved"),
    path("donate/", donate_view, name="donate"),
    #path("shop/", shop_view, name="shop"),
    path("subscribe/", subscribe_view, name="subscribe"),
    path("volunteer/", volunteer_view, name="volunteer"),
    path("community/", community_view, name="community")

]