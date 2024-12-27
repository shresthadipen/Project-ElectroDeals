from django.shortcuts import render
from .models import Signup
from django.views import View
from django.views.generic import TemplateView
# Create your views here.

# Login view
class LoginView(TemplateView):
    template_name = "login.html"

# Signup view
class SignupView(View):
    template_name = "signup.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = request.POST
        signup_username = data.get('signup-username')
        signup_email = data.get('signup-email')
        signup_password = data.get('signup-password')

        Signup.objects.create(
            signup_username=signup_username,
            signup_email=signup_email,
            signup_password=signup_password
        )
        return redirect('login')
