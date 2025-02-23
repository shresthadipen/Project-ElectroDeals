from django.urls import path
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .views import home, product, base, about, product_list, updateItem, cart, checkout, buy_now, order_history, process_order, profile, payment
=======
from .views import home, product, base, about, product_list, updateItem, cart, checkout, buy_now, order_history, process_order, profile, payment, search_products
>>>>>>> 552dea05ff3c91792d910b47f2e96a89dd8bfd8b

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
=======
    path('search/', search_products, name='search_products'),
>>>>>>> 552dea05ff3c91792d910b47f2e96a89dd8bfd8b
    path('process_order/', process_order, name='process_order'),
    path('order_history', order_history, name='order_history'),
    path('profile/', profile, name='profile'),
    path('payment/', payment, name='payment'),

]
