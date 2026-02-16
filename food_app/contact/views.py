from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Contact

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send mail to admin
        send_mail(
            subject=f"New Contact Query from {name}",
            message=f"Email: {email}\n\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")