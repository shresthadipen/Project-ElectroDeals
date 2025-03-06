from django.shortcuts import render, get_object_or_404, redirect

from django.core.exceptions import ValidationError
from ecommerce.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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

@login_required
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


# ------------search result view------------

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



# ----------------detail view -----------------
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

def user_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    message = ContactUs.objects.all().order_by("-id")

    return render(
        request,
        "details/user_details.html",
        {
            "customer": customer,"messages" : message
        },
    )

def order_detail(request, order_transaction_id):
    order = get_object_or_404(Order, transaction_id=order_transaction_id)
    message = ContactUs.objects.all().order_by("-id")
    
    return render(request, 'details/order_details.html', { "order": order, "messages" : message})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id= brand_id)
    message = ContactUs.objects.all().order_by("-id")
    
    return render(request, 'details/brand_details.html', { "brand": brand, "messages" : message})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id= category_id)
    message = ContactUs.objects.all().order_by("-id")
    
    return render(request, 'details/category_details.html', { "category": category, "messages" : message})
def message_detail(request, message_id):
    form = get_object_or_404(ContactUs, id= message_id)
    message = ContactUs.objects.all().order_by("-id")
    
    return render(request, 'details/message_details.html', { "form": form, "messages" : message})


# --------------Add-------------

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        brand_id = request.POST.get('brand')
        description = request.POST.get('description')
        display = request.POST.get('display')
        ram = request.POST.get('ram')
        storage = request.POST.get('storage')
        battery = request.POST.get('battery')
        processor = request.POST.get('processor')
        camera = request.POST.get('camera')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        message = ContactUs.objects.all().order_by("-id")


        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None 

        try:
            brand = Brand.objects.get(id=brand_id)
        except Brand.DoesNotExist:
            brand = None 

        if not name or not price or not image:
            return render(request, 'add/add_product.html', {'error': 'Please fill all required fields.'})

        try:
            product = Product(
                name=name,
                price=price,
                category=category,
                brand=brand,
                description=description,
                display=display,
                ram=ram,
                storage=storage,
                battery=battery,
                processor=processor,
                camera=camera,
                stock=stock,
                image=image
            )

            product.save()

            return redirect('product_dash', {"messages" : message}) 
        except ValidationError as e:
            return render(request, 'add/add_product.html', {'error': 'Validation Error: ' + str(e)})
    else:
        
        return render(request, 'add/add_product.html')

def add_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')


        try:
            brand = Brand(
                name=name,
                image=image
            )

            brand.save()

            return redirect('brand_dash') 
        except ValidationError as e:
            return render(request, 'add/add_brand.html', {'error': 'Validation Error: ' + str(e)})
    else:
        
        return render(request, 'add/add_brand.html')
    

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')


        try:
            category = Category(
                name=name,
                image=image
            )

            category.save()

            return redirect('category_dash') 
        except ValidationError as e:
            return render(request, 'add/add_category.html', {'error': 'Validation Error: ' + str(e)})
    else:
        
        return render(request, 'add/add_category.html')


# ---------Edit-----------
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    categories = Category.objects.all()
    brands = Brand.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        display = request.POST.get('display')
        ram = request.POST.get('ram')
        storage = request.POST.get('storage')
        battery = request.POST.get('battery')
        processor = request.POST.get('processor')
        camera = request.POST.get('camera')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')

        product.name = name
        product.price = price
        product.category_id = category
        product.brand_id = brand
        product.description = description
        product.display = display
        product.ram = ram
        product.storage = storage
        product.battery = battery
        product.processor = processor
        product.camera = camera
        product.stock = stock

        if image:
            product.image = image

        try:
            product.save()  
            return redirect('product_detail', product_id=product.id)
        except ValidationError as e:
            return render(request, 'edit/product_edit.html', {'product': product, 'categories': categories, 'brands': brands, 'error': str(e)})

    return render(request, 'edit/product_edit.html', {'product': product, 'categories': categories, 'brands': brands})
