from django.shortcuts import render
from .models import Brand, Category, Product

def home(request):
    brands = Brand.get_all_brand()[:8]
    category = Category.get_all_category()
    product = Product.get_all_product()[:5]


    return render(request, "home_page.html", {'brand' : brands, 'category' : category, 'product' : product})

def product(request):
    return render(request, "product.html")

def base(request):
    return render(request, "base.html")

def about(request):
    return render(request,"about_us.html")