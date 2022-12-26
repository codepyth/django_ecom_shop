from django.shortcuts import render
from .models import Product, Cartitems, Cart
# Create your views here.


def store(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity' : 0}

    context = {}

    products = Product.objects.all()

    context['products'] = products
    context['cart'] = cart
    context['cartitems'] = cartitems

    return render(request, 'cart/store.html', context)


def cart(request):
    context = {}

    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity' : 0}

    context['cart'] = cart
    context['cartitems'] = cartitems

    return render(request, 'cart/cart.html', context)