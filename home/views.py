from django.shortcuts import redirect , render
from django.views import View
from django.views.generic import TemplateView

# Home view
class HomeView(TemplateView):
    template_name = "home_page.html"

# Product view
class ProductView(TemplateView):
    template_name = "product.html"
