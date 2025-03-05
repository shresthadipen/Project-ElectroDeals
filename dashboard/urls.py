from django.urls import path
from .views import (dashboard, product_dash,brand_dash,category_dash,customer_dash,message_dash,
                    dashboard_home,order_dash,setting_dash,
                    search_products_dash, search_category_dash, 
                    search_order_dash, search_brand_dash, search_message_dash, 
                    search_customer_dash, product_detail)

urlpatterns = [
     path('dashboard/', dashboard_home, name='dashboard'),
    path('brand_dash/', brand_dash, name='brand_dash'),
    path('category_dash/', category_dash, name='category_dash'),
    path('customer_dash/', customer_dash, name='customer_dash'),
    path('message_dash/', message_dash, name='message_dash'),
    path('order_dash/', order_dash, name='order_dash'),
    path('product_dash/', product_dash, name='product_dash'),
    path('setting_dash/', setting_dash, name='setting_dash'),
    path('search_product_dash/', search_products_dash, name='search_products_dash'),
    path('search_order_dash/', search_order_dash, name='search_order_dash'),
    path('search_category_dash/', search_category_dash, name='search_category_dash'),
    path('search_brand_dash/', search_brand_dash, name='search_brand_dash'),
    path('search_customer_dash/', search_customer_dash, name='search_customer_dash'),
    path('search_message_dash/', search_message_dash, name='search_message_dash'),


# details page
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),


]
