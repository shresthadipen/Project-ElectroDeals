from django.urls import path
from .views import home,  product,  base ,about


urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('base/', base, name='base'),
    path('about/',about, name = 'about_us'),
    
]