import json
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .models import *


@csrf_exempt
def create_checkout_session(request):
    request_data = json.loads(request.body)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    line_items = []

    for item in order.orderitem_set.all():
        line_item = {
            "price_data": {
                "currency": "DKK",
                "product_data": {
                    "name": item.product.name,
                },
                "unit_amount": int(item.product.price * 100),
            },
            "quantity": item.quantity,
        }
        line_items.append(line_item)

    checkout_session = stripe.checkout.Session.create(
        customer_email=request_data["email"],
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=request.build_absolute_uri(reverse("success"))
        + "?transaction_id={CHECKOUT_transaction_id}",
        cancel_url=request.build_absolute_uri(reverse("success")),
    )

    order.stripe_payment_intent = checkout_session["payment_intent"]
    order.amount = int(item.product.price * 100)
    order.save()

    return JsonResponse({"sessionId": checkout_session.id})


def PaymentSuccessView(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer, complete=False)
    order.orderitem_set.all().delete()

    return render(request, "payments/success.html")


class PaymentFailedView(TemplateView):
    template_name = "failed.html"


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all().order_by("product__name")
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
        cartItems = order["get_cart_items"]

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "payments/checkout.html", context)
