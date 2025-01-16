from django.urls import path
from .views import home,  product,  base


urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('base/', base, name='base'),
    
]