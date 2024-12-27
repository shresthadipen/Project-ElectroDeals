from django.db import models

# Create your models here.
class Signup(models.Model):
    signup_username = models.CharField(max_length=100)
    signup_email = models.EmailField()
    signup_password = models.CharField(max_length=20)

