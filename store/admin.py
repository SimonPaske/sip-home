from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ("id", "name", "price", "category")
    search_fields = ["id", "name", "order", "transaction_id"]


@admin.register(Order)
class OrderAdmin(SummernoteModelAdmin):
    list_display = ("id", "customer", "complete", "transaction_id",
                    "order_date")
    list_filter = ("id", "customer", "complete", "order_date", "customer")


@admin.register(OrderItem)
class OrderItemAdmin(SummernoteModelAdmin):
    list_display = ("id", "product", "customer", "quantity", "date_added")
    list_filter = ("id", "product", "quantity", "date_added")


@admin.register(ProductReview)
class ProductReviewAdmin(SummernoteModelAdmin):
    list_display = ("product", "customer", "rating", "feedback", "date_added")
    list_filter = ("product", "customer", "rating", "date_added")
    search_fields = ("product__name", "customer__user__username", "feedback")