from django.urls import path
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .views import home, product, base, about, product_list, updateItem, cart, checkout, buy_now,search_products
=======
from .views import home, product, base, about, product_list, updateItem, cart, checkout, buy_now, order_history, process_order, profile, payment
>>>>>>> 203f78e666da1d930ed0d34d3b17f2cd616d2573

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product, name='product'), 
    path('base/', base, name='base'),
    path('about/', about, name='about_us'),
    path('product_list/', product_list, name='product_list'),
    path('update_item/', updateItem, name='update_item'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name="checkout"),
    path('buy-now/<int:product_id>/', buy_now, name='buy_now'),
<<<<<<< HEAD
    path('search/', search_products, name='search_products'),
=======
    path('process_order/', process_order, name='process_order'),
    path('order_history', order_history, name='order_history'),
    path('profile/', profile, name='profile'),
    path('payment/', payment, name='payment'),

>>>>>>> 203f78e666da1d930ed0d34d3b17f2cd616d2573
]
