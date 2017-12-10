from django.shortcuts import render

def home(request):
    return render(request, 'store/base.html')

def shop(request):
    return render(request, 'store/shop.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    return render(request, 'store/contact.html')

def values(request):
    return render(request, 'store/values.html')
