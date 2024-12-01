from django.shortcuts import render, redirect
from .models import Signup
# Create your views here.
def home (request):
    return render(request, "home_page.html")
        
def login (request):
    return render(request, "login.html")


def signup (request):
    if request.method ==  "POST":
        data = request.POST
        signup_username = data.get('signup-username')
        signup_email = data.get('signup-email')
        signup_password = data.get('signup-password')

        Signup.objects.create(
            signup_username = signup_username,
            signup_email = signup_email,
            signup_password =signup_password
        )
        return redirect('signup')
    return render(request, "signup.html")

def product (request):
    return render(request, "product.html")