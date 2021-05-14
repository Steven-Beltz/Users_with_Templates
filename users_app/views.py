from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_users" : User.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    age = request.POST['age']
    # print("Post works")
    # User.objects.create(first_name="firstName", last_name="lastName", email_address="email", age=28)
    User.objects.create(first_name=f"{firstName}", last_name=f"{lastName}", email_address=f"{email}", age=f"{age}")
    return redirect("/")