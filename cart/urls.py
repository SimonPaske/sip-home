from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("get_user/", get_user, name="get_user"),
    path("update_cart/", views.update_cart, name="update_cart"),
]
