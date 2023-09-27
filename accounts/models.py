from django.contrib.auth.models import User
from django.db import models



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=80, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name if self.name else "No Name"
