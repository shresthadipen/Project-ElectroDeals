from django.contrib import admin
from .models import Category, Product, Brand, Customer, Order, OrderItem, ShippingAddress,ContactUs

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'brand', 'description', 'ram', 'storage', 'battery', 'processor', 'camera','stock',]

class AdminBrand(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'complete', 'transaction_id', 'date_ordered']


class AdminOrderItem(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'date_added']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
    

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Brand, AdminBrand)
admin.site.register(Category)
admin.site.register(Product, AdminProduct)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderItem, AdminOrderItem)
admin.site.register(ShippingAddress)


