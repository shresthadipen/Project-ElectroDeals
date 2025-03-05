from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('signup-username')
        email = request.POST.get('signup-email')
        password = request.POST.get('signup-password')
        confirm_password = request.POST.get('signup-confirm-password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, "Succesful account")
        return redirect('login')

    return render(request, 'signup.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            if user.is_superuser: 
                return redirect('dashboard') 

            return redirect('home')  

        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


def logout_view(request):
    logout(request) 
    messages.success(request, "Logged out successfully.")
    return redirect('home')

