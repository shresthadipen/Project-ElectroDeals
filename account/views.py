from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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


def login_view(request):

    if request.method == "POST":
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')

        user = authenticate(username = username, password = password )

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, 'login.html')























    #     try:
    #         if User.objects.filter(username=signup_username).exists():
    #             messages.error(request, "Username already exists.")
    #             return redirect('signup')
    #         if User.objects.filter(email=signup_email).exists():
    #             messages.error(request, "Email is already registered.")
    #             return redirect('signup')

    #         User.objects.create_user(
    #             username=signup_username,
    #             email=signup_email,
    #             password=signup_password
    #         )
    #         return redirect('login')
    #     except Exception as e:
    #         messages.error(request, f"An error occurred: {str(e)}")
    #         return redirect('signup')

    # return render(request, 'signup.html')
