from django.shortcuts import render

from .models import CONTAINERS, ORDERS, collect_cart




def index(request):
    template = "transport/index.html"
    context = {
        "title": "Контейнеры",
        "containers": CONTAINERS,
        "collected_cart": collect_cart(),
    }
    return render(request, template, context)


def cart(request):
    template = "transport/cart.html"
    context = {
        "title": "Корзина",
    }
    return render(request, template, context)


def cont(request, id):
    template = "transport/cont.html"
    context = {
        "title": "Контейнер",
    }
    return render(request, template, context)


def add_product_to_cart(request, id):
    template = "transport/cart.html"
    context = {
        "title": "Корзина",
        "products": "Продукт 1",
    }
    return render(request, template, context)