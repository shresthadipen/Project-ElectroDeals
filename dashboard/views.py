from django.shortcuts import render
from ecommerce.models import *

# Create your views here.
def dashboard(request):
    brands = Brand.get_all_brand()[:10]
    category = Category.get_all_category()
    products = Product.objects.all().order_by('-id')[:7]  
    return render(request, "dashboard.html", 
            {"brand": brands,
            "category": category,
            "products": products,
            })