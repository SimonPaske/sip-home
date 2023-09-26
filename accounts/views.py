from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import *
from .models import *


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("store")

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()
            customer, created = Customer.objects.get_or_create(user=user)
            customer.name = user.username
            customer.email = user.email
            customer.save()

            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("store")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")

    else:
        form = NewUserForm()

    return render(request, "accounts/register.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("store")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("store")
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, "accounts/login.html", {"page": "login"})


def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("login")


@login_required(login_url="login")
def edit_customer(request):
    customer = request.user.customer

    if request.method == "POST":
        form = EditCustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("store")

    else:
        form = EditCustomerForm(instance=customer)

    return render(request, "accounts/edit_profile.html", {"form": form})
