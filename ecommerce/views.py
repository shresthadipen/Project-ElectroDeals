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

def product_list(request):
    brand_filter = request.GET.get('brand')
    category_filter = request.GET.get('category')

    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    if brand_filter:
        products = products.filter(brand__name=brand_filter)
    if category_filter:
        products = products.filter(category__name=category_filter)

    return render(request, 'filtered_products.html', { 
        'products': products,
        'brands': brands,
        'categories': categories,
    })

