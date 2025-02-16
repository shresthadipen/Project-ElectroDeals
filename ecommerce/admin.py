from django.contrib import admin
from .models import Category, Product, Brand, Customer, Order, OrderItem, ShippingAddress

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'brand', 'description']

class AdminBrand(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']


admin.site.register(Brand, AdminBrand)
admin.site.register(Category)
admin.site.register(Product, AdminProduct)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


