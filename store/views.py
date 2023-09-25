import json
from typing import Any
from store.forms import ProductReviewForm
import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from store.models import Customer, Order, OrderItem, Product, ProductReview


@login_required(login_url="login")
def store(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except ObjectDoesNotExist:
            customer = Customer.objects.create(user=request.user)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "cart_cart_items": 0, "shipping": False}
        cartItems = order["get_cart_items"]

    products = Product.objects.all().order_by("name")
    context = {"products": products, "cartItems": cartItems}
    return render(request, "store/store.html", context)


def contact(request):
    context = {
        "page": "contact",
        "name": "Full Name",
        "email": "Email",
        "message": "Message",
    }
    return render(request, "store/contact.html")



class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["stripe_publishable_key"] = settings.STRIPE_PUBLISHABLE_KEY

        # Fetch the latest 3 reviews for the current product
        latest_reviews = ProductReview.objects.filter(product=self.object).order_by(
            "-date_added"
        )[:3]
        context["latest_reviews"] = latest_reviews

        all_reviews = ProductReview.objects.filter(product=self.object).order_by(
            "-date_added"
        )
        context["all_reviews"] = all_reviews
        return context

    def process_payment(request):
        if request.method == 'POST':
            amount = 1000  # $10 in cents

            # Create a PaymentIntent on Stripe
            stripe.api_key = settings.STRIPE_SECRET_KEY
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='DKK',
            )

            return render(request, 'payments/payment_form.html', {'client_secret': intent.client_secret})


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "product_list"


def add_product_review(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        if request.method == "POST":
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = ProductReview()
                review.product = product
                review.customer = request.user.customer
                review.rating = float(request.POST["rating"])
                review.feedback = request.POST["feedback"]
                review.save()
                messages.success(
                    request, "Your review has been submitted successfully."
                )
                return redirect("detail", id=product_id)
            else:
                print("Form Errors:", form.errors)
        else:
            form = ProductReviewForm()

    return render(
        request, "product_review.html", {"form": form, "product": product}
    )
