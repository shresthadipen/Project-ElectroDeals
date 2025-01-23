from django.shortcuts import render


def home(request):
    return render(request, "home_page.html")

def product(request):
    return render(request, "product.html")

def base(request):
    return render(request, "base.html")

def about(request):
    return render(request,"about_us.html")