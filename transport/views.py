from django.shortcuts import render


def index(request):
    template = "transport/index.html"
    context = {
        "title": "Контейнеры",
        "containers": [
            {
                "id": 1,
                "name": "Контейнер 1",
                "description": "Описание контейнера 1",
                "image": "container1.jpg",
                "items": [],
            },
            {
                "id": 2,
                "name": "Контейнер 2",
                "description": "Описание контейнера 2",
                "image": "container2.jpg",
            },
            {
                "id": 3,
                "name": "Контейнер 3",
                "description": "Описание контейнера 3",
                "image": "container3.jpg",
            }
        ]
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