from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'address')
    list_filter = ['id', 'first_name', 'email']
    search_fields = ['id', 'email', 'product', 'transaction_id']
 


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ['id', 'name', 'order', 'transaction_id']
    


@admin.register(Order)
class OrderAdmin(SummernoteModelAdmin):
    list_display = ('id', 'customer', 'complete',
                    'transaction_id', 'order_date')
    list_filter = ('id', 'customer', 'complete', 'order_date', 'customer')
   

@admin.register(OrderItem)
class OrderItemAdmin(SummernoteModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity', 'date_added')
    list_filter = ('id', 'product', 'order', 'quantity', 'date_added')
    search_fields = ['id', 'product', 'order', 'quantity', 'date_added']
  


@admin.register(ShippingAddress)
class ShippingAddressAdmin(SummernoteModelAdmin):
    list_display = ('id', 'customer', 'order', 'address',
                    'street_and_city', 'country')
    list_filter = ('id', 'customer', 'order', 'address',
                   'street_and_city', 'country')
    search_fields = ['id', 'customer', 'order',
                     'address', 'street_and_city', 'country']



@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('id', 'product', 'customer', 'rating', 'date_added')
    summernote_fields = ('feedback')
