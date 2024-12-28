from django.urls import path
from .views import HomeView, ProductView

app_name = 'home' 

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/', ProductView.as_view(), name='product'),
    
]