from django.shortcuts import render


def home(request):
    return render(request, "home_page.html")

def product(request):
    return render(request, "product.html")