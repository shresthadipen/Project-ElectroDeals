from django.contrib import admin
from .models import Category, Product, Brand

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'brand', 'description']


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, AdminProduct)
