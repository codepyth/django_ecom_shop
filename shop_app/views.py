from django.shortcuts import render

# Create your views here.


def store(request):
    context = {}

    return render(request, 'cart/store.html', context)


def cart(request):
    context = {}

    return render(request, 'cart/cart.html', context)