from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("failed/", PaymentFailedView.as_view(), name="failed"),
    path("success/", views.PaymentSuccessView, name="success"),
    path("api/checkout-session/", create_checkout_session, name="api_checkout_session"),
]
