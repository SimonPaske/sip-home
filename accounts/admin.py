from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    list_display = ("id", "name", "email", "address")
    list_filter = ["id", "name", "email"]
    search_fields = ["id", "email", "product", "transaction_id"]
