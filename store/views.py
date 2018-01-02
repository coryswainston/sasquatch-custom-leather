from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'store/base.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products})

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    return render(request, 'store/contact.html')

def values(request):
    return render(request, 'store/values.html')
