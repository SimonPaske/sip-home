from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request, 'store/store.html')

def cart(request):
    context = {}
    return render(request, 'store/cart.html')

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html')

def mystery(request):
    context = {}
    # You can use the 'category' parameter to filter your products
    # and render the appropriate template
    # Example: products = Product.objects.filter(category=category)
    return render(request, 'store/mystery.html')

def otherstuff(request):
    context = {}
    return render(request, 'store/otherstuff.html')

def nature(request):
    context = {}
    return render(request, 'store/nature.html')

def contact(request):
    context = {}
    return render(request, 'store/contact.html')