from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import home, product, base, about, product_list, updateItem, cart, checkout, buy_now

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
]
