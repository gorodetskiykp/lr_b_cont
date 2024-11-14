from django.shortcuts import render


def check(request):
    template = "transport/check.html"
    context = {}
    return render(request, template, context)


def containers(request):
    template = "transport/containers.html"
    context = {
        "containers": [
            {"number": 324532432, "weight": 5488},
            {"number": 543534534, "weight": 5481},
            {"number": 654324444, "weight": 5484},
            {"number": 897684565, "weight": 5233},
        ],
    }
    return render(request, template, context)


