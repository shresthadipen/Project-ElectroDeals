from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand, Category, Product, Order, OrderItem, Customer, ShippingAddress,ContactUs
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import json

def home(request):
    brands = Brand.get_all_brand()[:10]
    category = Category.get_all_category()
    products = Product.objects.all().order_by('-id')[:7]  
    cartItem = cart_items(request)
    product = Product.objects.filter(name='Galaxy s25 Ultra').first()
    return render(
        request,
        "home_page.html",
        {
            "brand": brands,
            "category": category,
            "products": products,
            "cartItems": cartItem["cartItems"],
            'product': product,
        },
    )



def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cartItem = cart_items(request)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)

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
    
    return render(request, "about_us.html",{"cartItems": cartItem["cartItems"]})

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        cartItem = cart_items(request)


        ContactUs.objects.create(name=name, email=email, message=message)
        return redirect("contact")  # Redirect after form submission

    return render(request, "about_us.html")

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

@login_required
def cart(request):
    customer = get_customer(request)
    if customer:
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    cartItem = cart_items(request)
    return render(
        request, "cart.html", {"items": items, "order": order, "cartItems": cartItem["cartItems"]}
    )


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        order.delete()

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
                    if product.stock > 0:  
                        orderItem.quantity += 1
                        product.stock -= 1  
                    else:
                        return JsonResponse({'error': 'Out of stock'}, status=400)

                elif action == 'remove' and orderItem.quantity > 0:
                    orderItem.quantity -= 1
                    product.stock += 1  

                orderItem.save()
                product.save()

                if orderItem.quantity <= 0:
                    orderItem.delete()

                if action == 'delete':
                    orderItem.delete()

                return JsonResponse({'message': 'Item updated successfully', 'quantity': orderItem.quantity, 'stock': product.stock}, safe=False)

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
        cartItems = request.session.get("cart_items", 0)
    return {"cartItems": cartItems}


def get_customer(request):
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        return customer
    return None


def buy_now(request, product_id):
    product = Product.objects.get(id=product_id)
    
    request.session['buy_now_product'] = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'image': product.image.url
    }
    
    return redirect('checkout')


@login_required
def order_history(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer, complete=True).order_by("-date_ordered")
    cartItem = cart_items(request)  

    return render(request, "order.html", {"orders": orders, "cartItems": cartItem.get("cartItems", 0)})


def profile(request):
    username = request.user.username
    email = request.user.email
    cartItem = cart_items(request)
    return render(request, "profile.html", {"username": username, "email": email, 'cartItems': cartItem["cartItems"]})


def process_order(request):
    if request.method == 'POST':
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        order.transaction_id = Order.get_next_transaction_id()  

        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['zip']
        phone = request.POST['phone']

        shipping_address = ShippingAddress(
            customer=customer,
            order=order,
            address=address,
            city=city,
            state='',  
            zipcode=zip_code
        )
        shipping_address.save()

        order.payment_method = "Cash on Delivery"
        order.complete = True 
        order.delivered = False  
        order.save()
        return redirect('order_history') 
        
    
    return redirect('checkout')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password has been successfully updated!')
            return redirect('profile') 
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form,})


def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query) | Product.objects.filter(brand__name__icontains=query) | Product.objects.filter(category__name__icontains=query)
    products = products.distinct()  
    
    cartItem = cart_items(request)

    return render(request, 'search.html', {
        'products': products,
        'cartItems': cartItem["cartItems"]
    })

def generate_bill(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user.customer, complete=True)
    order_items = OrderItem.objects.filter(order=order)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order_id}.pdf"'

    
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle(f"Invoice #{order.id}")

    
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 750, "ElectroDeals Invoice")
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 720, f"Order ID: {order.id}")
    pdf.drawString(50, 700, f"Customer: {request.user.username.capitalize()}")
    
    pdf.drawString(50, 670, "--------------------------------------------------------------------------------------------------------------------------")
    
    
    y_position = 650
    pdf.drawString(50, y_position, "Product")
    pdf.drawString(250, y_position, "Quantity")
    pdf.drawString(350, y_position, "Price")
    pdf.drawString(450, y_position, "Total")
    
    y_position -= 20
    pdf.drawString(50, y_position, "--------------------------------------------------------------------------------------------------------------------------")

    
    for item in order_items:
        y_position -= 20
        pdf.drawString(50, y_position, item.product.name)
        pdf.drawString(250, y_position, str(item.quantity))
        pdf.drawString(350, y_position, f"Rs {item.product.price}")
        pdf.drawString(450, y_position, f"Rs {item.get_total}")

    
    y_position -= 40
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y_position, f"Grand Total: Rs {order.get_cart_total}")

    pdf.showPage()
    pdf.save()

    return response

