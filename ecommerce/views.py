from django.shortcuts import render, get_object_or_404
from .models import (
    Brand,
    Category,
    Product,
    Customer,
    Order,
    OrderItem,
    ShippingAddress,
)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    brands = Brand.get_all_brand()[:10]
    category = Category.get_all_category()
    products = Product.get_all_product()[:5]
    cartItem = cart_items(request)

    return render(
        request,
        "home_page.html",
        {
            "brand": brands,
            "category": category,
            "products": products,
            "cartItems": cartItem["cartItems"],
        },
    )


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cartItem = cart_items(request)
    related_products = Product.objects.exclude(id=product_id)

    return render(
        request,
        "product.html",
        {
            "product": product,
            "related_products": related_products,
            "cartItems": cartItem["cartItems"],
        },
    )


def base(request):
    cartItem = cart_items(request)
    return render(request, "base.html", {"cartItems": cartItem["cartItems"]})


def about(request):
    cartItem = cart_items(request)
    return render(request, "about_us.html", {"cartItems": cartItem["cartItems"]})


def product_list(request):
    brand_filter = request.GET.get("brand")
    category_filter = request.GET.get("category")

    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    cartItem = cart_items(request)

    if brand_filter:
        products = products.filter(brand__name=brand_filter)
    if category_filter:
        products = products.filter(category__name=category_filter)

    return render(
        request,
        "filtered_products.html",
        {
            "products": products,
            "brands": brands,
            "categories": categories,
            "cartItems": cartItem["cartItems"],
        },
    )


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    cartItem = cart_items(request)
    return render(
        request,
        "cart.html",
        {"items": items, "order": order, "cartItems": cartItem["cartItems"]},
    )


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    cartItem = cart_items(request)
    return render(
        request,
        "checkout.html",
        {"items": items, "order": order, "cartItems": cartItem["cartItems"]},
    )

@csrf_exempt
def updateItem(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            productId = data.get('productId')
            action = data.get('action')

            if request.user.is_authenticated:
                customer = request.user.customer
                product = Product.objects.get(id=productId)
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

                if action == 'add':
                    orderItem.quantity += 1
                elif action == 'remove':
                    orderItem.quantity -= 1
                print("Okk")
                orderItem.save()

                if orderItem.quantity <= 0:
                    orderItem.delete()

                return JsonResponse({'message': 'Item updated successfully', 'quantity': orderItem.quantity}, safe=False)

            return JsonResponse({'error': 'User not authenticated'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def cart_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        # For anonymous users, we can store the cart items in the session
        cartItems = request.session.get("cart_items", 0)
    return {"cartItems": cartItems}