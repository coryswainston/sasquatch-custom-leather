from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .models import Cart

def get_name(request):
    name = None
    if (request.user.is_authenticated):
        name = request.user.first_name
    return name;

def home(request):
    return render(request, 'store/base.html', {'user_name': get_name(request)})

def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products, 'user_name': get_name(request)})

def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        products = cart.products.all()
        if (request.method == "POST"):
            pk = request.POST.__getitem__("product_pk")
            product = get_object_or_404(Product, pk=pk)
            product.quantity -= 1
            product.save()
            if (product.quantity == 0):
                product.save()
                cart.products.remove(product)
                cart.save()
        cost = get_total_cost(products)
        return render(request, 'store/cart.html', {'products': products, 'total_cost': cost, 'user_name': get_name(request)})
    except Cart.DoesNotExist:
        cart = Cart()
        cart.user = request.user
        cart.save()
        products = cart.products.all()
    return render(request, 'store/cart.html', {'products': products, 'total_cost': 0, 'user_name': get_name(request)})

def get_total_cost(products):
    cost = 0
    for product in products:
        cost += product.price * product.quantity
    return cost

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    return render(request, 'store/contact.html', {'user_name': get_name(request)})

def values(request):
    return render(request, 'store/values.html', {'user_name': get_name(request)})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        try:
            cart = Cart.objects.get(user=request.user)
            cart.products.add(product)
            product.quantity += 1
            product.save()
            cart.save()
            return redirect('cart')
        except Cart.DoesNotExist:
            cart = Cart()
            cart.user = request.user
            cart.products.add(product)
            product.quantity += 1
            product.save()
            cart.save()
            return redirect('cart')
    else:
        return render(request, 'store/product_detail.html', {'product': product, 'user_name': get_name(request)})
