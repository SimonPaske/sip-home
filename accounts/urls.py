from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("edit_profile/", views.edit_customer, name="edit_profile"),
    
]
