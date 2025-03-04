from django.shortcuts import render
from ecommerce.models import *


# Create your views here.
def dashboard(request):
    brands = Brand.get_all_brand().order_by("-id")
    category = Category.get_all_category().order_by("-id")
    products = Product.objects.all().order_by("-id")
    order = Order.get_all_order().order_by("-id")
    customer = Customer.objects.all().order_by("-id")
    message = ContactUs.objects.all().order_by("-id")

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

        },
    )
