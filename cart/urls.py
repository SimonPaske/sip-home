from django.urls import path, include
# from payments.views import checkout
from . import views
from .views import *


urlpatterns = [
    path('', views.cart, name="cart"),
    path("get_user/", get_user, name="get_user"),
    path("update_cart/", views.update_cart, name="update_cart"),
    path("cart/", views.cart, name="cart"),
    # path("checkout/", views.checkout, name="checkout"),
]
