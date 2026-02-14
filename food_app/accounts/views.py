from django.template import loader
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import LoginUser,SignupUser

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 1. Create the user
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # 2. Send the Welcome Email
            subject = "Welcome to Our Food Order!"
            message = f"Hi {username}, thanks for signing up. We're glad to have you!"
            message = f"Hope you will enjoy the food :)"
            message = f"Order Eat Enjoy"
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email], # Send to the email the user just typed in
                    fail_silently=False,
                )
            except Exception as e:
                # Log the error but don't stop the user from signing up
                print(f"Mail error: {e}")

            messages.success(request, "Account created! Please Check your email.")
            return redirect('login') 

    return render(request, "signup.html")


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('login-user')
        password = request.POST.get('login-pass')

        # This checks the built-in User model and verifies the hashed password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # Creates the session
            
            # --- Send Login Email ---
            try:
                send_mail(
                    "New Login Alert",
                    f"Hi {user.username}, you just logged in to your Food Order account.",
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Login mail error: {e}")
            # ------------------------

            messages.success(request, f"Welcome, {username}")
            return redirect("home")
        else:
            # If authenticate returns None, the credentials were wrong
            messages.error(request, "Invalid username or password")
        
    return render(request, "login.html")

def logout(request):
    return redirect("login")