from django.shortcuts import render
from .models import Brand, Category

def home(request):
    brands = Brand.get_all_brand()[:6]
    category = Category.get_all_category()

    return render(request, "home_page.html", {'brand' : brands, 'category' : category})

def product(request):
    return render(request, "product.html")

def base(request):
    return render(request, "base.html")

def about(request):
    return render(request,"about_us.html")