from accounts.models import Customer
from store.models import Order
from django.db import models


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    street_and_city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address