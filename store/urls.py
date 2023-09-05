from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name='checkout'),
    path('mystery/', views.mystery, name='mystery'),
    path('nature/', views.nature, name='nature'),
    path('otherstuff/', views.otherstuff, name='otherstuff'),
]
