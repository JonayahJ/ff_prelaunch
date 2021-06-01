from django.shortcuts import render, redirect
from .models import Email
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def email(request):
    if request.method == "POST":
        signup_email    =   request.POST["signup_email"]

        email = Email(signup_email=signup_email)

        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email
        send_mail(
            'You have a new subscriber waiting for you!',
            'A potential client or interested party signed up on the prelaunch site.  Please login to the admin panel to see more details.',
            'support@fourfront.io',
            [admin_email],
            fail_silently=False,
        )

        email.save()
        return redirect("/thank-you")
        