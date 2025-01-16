from django.contrib import admin
from .models import Category, Product, Brand

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'brand', 'description']

class AdminBrand(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']


admin.site.register(Brand, AdminBrand)
admin.site.register(Category)
admin.site.register(Product, AdminProduct)
