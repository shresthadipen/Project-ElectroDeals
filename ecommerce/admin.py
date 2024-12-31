from django.contrib import admin
from .models import Category, Product

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price','category','description' ]

admin.site.register(Category)
admin.site.register(Product, AdminProduct)
