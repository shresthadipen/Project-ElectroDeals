from django.urls import path
from .views import home,  product,  base ,about,product_list


urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('base/', base, name='base'),
    path('about/',about, name = 'about_us'),
    path('product_list/',product_list,name='product_list')
]