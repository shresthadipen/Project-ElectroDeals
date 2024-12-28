from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages  


def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        signup_username = request.POST.get('signup-username')
        signup_email = request.POST.get('signup-email')
        signup_password = request.POST.get('signup-password')

        myuser = User.objects.create_user(signup_username, signup_email, signup_password)
        myuser.save()

        messages.success(request, "Succesful account")
        return redirect('login')

    return render(request, 'signup.html')

























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
