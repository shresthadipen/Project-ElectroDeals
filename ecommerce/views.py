from django.shortcuts import render, get_object_or_404
from .models import Brand, Category, Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    brands = Brand.get_all_brand()[:10]
    category = Category.get_all_category()
    products = Product.get_all_product()[:5]
    return render(request, "home_page.html", {'brand': brands, 'category': category, 'products': products})

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    related_products = Product.objects.exclude(id=product_id) 
    
    return render(request, "product.html", {'product': product, 'related_products': related_products})

def base(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about_us.html")

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


@csrf_exempt
def updateItem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        # Add your logic to update the cart here
        print('Product ID:', productId, 'Action:', action)

        return JsonResponse({'message': 'Item updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
