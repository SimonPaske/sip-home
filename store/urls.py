from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path("", ProductListView.as_view(), name="home"),
    path("detail/<id>/", ProductDetailView.as_view(), name="detail"),
    path("product/<int:product_id>/review/", views.add_product_review, name="add_product_review",),
]

