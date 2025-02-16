from django.urls import path
<<<<<<< HEAD
from .views import home, product, base, about, product_list
=======
from .views import home,  product,  base, about, product_list, updateItem

>>>>>>> c16ba94 (add to cart)

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product, name='product'), 
    path('base/', base, name='base'),
<<<<<<< HEAD
    path('about/', about, name='about_us'),
    path('product_list/', product_list, name='product_list'),
]
=======
    path('about/',about, name = 'about_us'),
    path('product_list/',product_list,name='product_list'),
    path('update_item/', updateItem, name='update_item'),
]
>>>>>>> c16ba94 (add to cart)
