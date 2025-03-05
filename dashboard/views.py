from django.shortcuts import render, get_object_or_404
from ecommerce.models import *
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime


# Create your views here.
def dashboard(request):
    brands = Brand.get_all_brand().order_by("-id")
    category = Category.get_all_category().order_by("-id")
    products = Product.objects.all().order_by("-id")
    order = Order.get_all_order().order_by("-id")
    customer = Customer.objects.all().order_by("-id")
    message = ContactUs.objects.all().order_by("-id")
    totalSales = Order.get_total_sales()
    totalOrders = Order.get_total_orders()
    totalUsers = Customer.get_total_user()


    return render(
        request,
        "dashboard.html",
        {
            "brand": brands,
            "category": category,
            "products": products,
            "orders" : order,
            "customers": customer,
            "messages" : message,
            "totalSales" : totalSales,
            "totalOrders" : totalOrders,
            "totalUsers" : totalUsers,


        },
    )


def dashboard_home(request):
    totalOrder = Order.get_total_orders()
    totalSales = Order.get_total_sales()
    totalUser = Customer.get_total_user()
    order = Order.get_all_order().order_by("-id")
    message = ContactUs.objects.all().order_by("-id")

    return render(request, "dashboardHome.html", {"totalOrder" : totalOrder, "totalSales" : totalSales, "totalUser" : totalUser, "orders": order, "messages" : message})

def category_dash(request):
    message = ContactUs.objects.all().order_by("-id")

    category = Category.get_all_category().order_by("-id")
    return render(request, "category_dash.html", { "category" : category, "messages" : message})

def customer_dash(request):
    message = ContactUs.objects.all().order_by("-id")

    customer = Customer.objects.all().order_by("-id")
    return render(request, "customer_dash.html", { "customers" : customer, "messages" : message})

def message_dash(request):
    message = ContactUs.objects.all().order_by("-id")

    message = ContactUs.objects.all().order_by("-id")
    return render(request, "message_dash.html", { "messages" : message})

def order_dash(request):
    message = ContactUs.objects.all().order_by("-id")

    order = Order.get_all_order().order_by("-id")
    return render(request, "order_dash.html", { "orders" : order, "messages" : message})

def brand_dash(request):
    message = ContactUs.objects.all().order_by("-id")

    brands = Brand.get_all_brand().order_by("-id")
    return render(request, "brand_dash.html", { "brand" : brands, "messages" : message})

def product_dash(request):
    message = ContactUs.objects.all().order_by("-id")

    products = Product.objects.all().order_by("-id")
    return render(request, "product_dash.html", { "products" : products, "messages" : message})

def setting_dash(request):
    message = ContactUs.objects.all().order_by("-id")

    return render(request, "setting_dash.html" , {"messages" : message})


def search_products_dash(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query) | Product.objects.filter(brand__name__icontains=query) | Product.objects.filter(category__name__icontains=query)
    products = products.distinct()  
    message = ContactUs.objects.all().order_by("-id")
    

    return render(request, 'search/search_product_dash.html', {
        'products': products, "messages" : message
    })

def search_order_dash(request):
    query = request.GET.get('query', '')

    orders = Order.objects.all()
    if query.lower() in ['true', 'false']:
        is_complete = query.lower() == 'true'
        orders = orders.filter(complete=is_complete)
    else:
        orders = orders.filter(
            Q(transaction_id__icontains=query) |
            Q(payment_method__icontains=query) | 
            Q(customer__name__icontains=query) |  
            Q(customer__user__username__icontains=query) 
        ).distinct()

    messages = ContactUs.objects.all().order_by("-id")

    return render(request, 'search/search_order_dash.html', {
        'orders': orders,
        'messages': messages
    })


def search_category_dash(request):
    query = request.GET.get('query', '') 
    if query:
        categories = Category.objects.filter(name__icontains=query)
    else:
        categories = Category.objects.all()  
    return render(request, 'search/search_category.html', {
        'category': categories
    })



def search_brand_dash(request):
    query = request.GET.get('query', '')
    brand = Brand.objects.filter(name__icontains=query) 
    brand = brand.distinct()  
    message = ContactUs.objects.all().order_by("-id")
    

    return render(request, 'search/search_brand.html', {
        'brand': brand, "messages" : message
    })


def search_message_dash(request):
    query = request.GET.get('query', '')
    
    message = ContactUs.objects.filter(name__icontains=query) | ContactUs.objects.filter(email__icontains=query)
    message = message.distinct() 

    messages = ContactUs.objects.all().order_by("-id")
    
    return render(request, 'search/search_message.html', {
        'message': message, 
        'messages': messages  
    })

def search_customer_dash(request):
    query = request.GET.get('query', '')
    customers = Customer.objects.filter(name__icontains=query) | Customer.objects.filter(email__icontains=query) 
    customers = customers.distinct()  
    message = ContactUs.objects.all().order_by("-id")
    

    return render(request, 'search/search_user.html', {
        'customers': customers, "messages" : message
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    message = ContactUs.objects.all().order_by("-id")

    return render(
        request,
        "details/product_details.html",
        {
            "product": product,"messages" : message
        },
    )