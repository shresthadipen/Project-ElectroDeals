from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import home, product, base, about, product_list, updateItem, cart, checkout, buy_now, order_history, process_order,change_password, profile, search_products

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
    path('search/', search_products, name='search_products'),
    path('process_order/', process_order, name='process_order'),
    path('order_history', order_history, name='order_history'),
    path('profile/', profile, name='profile'),
    path('change-password/', change_password, name='change_password'),
]
