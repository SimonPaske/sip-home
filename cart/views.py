import json
from django.http import JsonResponse
from django.shortcuts import render

from .models import *


# Create your models here.
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all().order_by("product__name")
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
        cartItems = order["get_cart_items"]

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "cart.html", context)

def update_cart(request):
    data = json.loads(request.body)
    product_id = data["productId"]
    action = data["action"]

    customer = request.user.customer
    product = Product.objects.get(id=product_id)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderitem.quantity += 1
        orderitem.save()
    elif action == "remove":
        if orderitem.quantity > 0:
            orderitem.quantity -= 1
            orderitem.save()
    if action == "delete":
        orderitem.delete()
    elif orderitem.quantity <= 0:
        orderitem.delete()

        OrderItem.objects.filter(order=order, product=product).delete()

    return JsonResponse("Item was updated.", safe=False)


def get_user(request):
    user = str(request.user)
    return JsonResponse({"user": user})