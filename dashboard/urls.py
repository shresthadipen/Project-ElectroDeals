from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/', dashboard_home, name='dashboard'),
    path('brand_dash/', brand_dash, name='brand_dash'),
    path('category_dash/', category_dash, name='category_dash'),
    path('customer_dash/', customer_dash, name='customer_dash'),
    path('message_dash/', message_dash, name='message_dash'),
    path('order_dash/', order_dash, name='order_dash'),
    path('product_dash/', product_dash, name='product_dash'),
    path('setting_dash/', setting_dash, name='setting_dash'),

    # ----------search----------
    path('search_product_dash/', search_products_dash, name='search_products_dash'),
    path('search_order_dash/', search_order_dash, name='search_order_dash'),
    path('search_category_dash/', search_category_dash, name='search_category_dash'),
    path('search_brand_dash/', search_brand_dash, name='search_brand_dash'),
    path('search_customer_dash/', search_customer_dash, name='search_customer_dash'),
    path('search_message_dash/', search_message_dash, name='search_message_dash'),


# details page
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('user_detail/<int:customer_id>/', user_detail, name='user_detail'),
    path('order_detail/<str:order_transaction_id>/', order_detail, name='order_detail'),
    path('brand_detail/<int:brand_id>/', brand_detail, name='brand_detail'),
    path('category_detail/<int:category_id>/', category_detail, name='category_detail'),
    path('message_detail/<int:message_id>/', message_detail, name='message_detail'),


    # -------------Add-------------
    path('add_product', add_product, name='add_product'),
    path('add_brand', add_brand, name='add_brand'),
    path('add_category', add_category, name='add_category'),

    # ------------Delete----------
    path('delete/<int:brand_id>/', delete_brand, name='delete_brand'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),



    # -------------Edit-----------
    path('product/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('brand_edit/<int:brand_id>/', edit_brand, name='edit_brand'),
    path('edit_category/<int:category_id>/', edit_category, name='edit_category'),



    
]
