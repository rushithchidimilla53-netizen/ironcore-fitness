from .data import BACK_EXERCISES
from .data import CHEST_EXERCISES
from .data import LEGS_EXERCISES
from .data import SHOULDERS_EXERCISES
from .data import ARMS_EXERCISES
from .data import CORE_EXERCISES
from .data import CARDIO_EXERCISES
from .data import FULLBODY_EXERCISES


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.forms import (
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

import razorpay
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from . import data



def home(request):
    context = {
        'active_page': 'home',
        'workout_categories': data.WORKOUT_CATEGORIES,
        'featured_plans': data.WORKOUT_PLANS[:3],
        'featured_diets': data.DIET_PLANS[:4],
        'featured_trainers': data.TRAINERS[:4],
        'transformation_images': data.TRANSFORMATION_IMAGES,
        'home_pricing': data.PRICING_PLANS,
        'testimonials_home': data.TESTIMONIALS,
    }
    return render(request, 'fitness/home.html', context)


def about(request):
    context = {'active_page': 'about', 'trainers': data.TRAINERS[:3]}
    return render(request, 'fitness/about.html', context)


def services(request):
    context = {'active_page': 'services', 'services': data.SERVICES}
    return render(request, 'fitness/services.html', context)


def workout_plans(request):
    context = {'active_page': 'workout_plans', 'plans': data.WORKOUT_PLANS,
               'categories': data.WORKOUT_CATEGORIES}
    return render(request, 'fitness/workout_plans.html', context)

@login_required(login_url='login')
def diet_plans(request):
    context = {'active_page': 'diet_plans', 'diets': data.DIET_PLANS}
    return render(request, 'fitness/diet_plans.html', context)


def trainers(request):
    context = {'active_page': 'trainers', 'trainers': data.TRAINERS}
    return render(request, 'fitness/trainers.html', context)

@login_required(login_url='login')
def bmi_calculator(request):
    return render(request, 'fitness/bmi_calculator.html', {'active_page': 'bmi_calculator'})

@login_required(login_url='login')
def calorie_calculator(request):
    return render(request, 'fitness/calorie_calculator.html', {'active_page': 'calorie_calculator'})

@login_required(login_url='login')
def workout_timer(request):
    return render(request, 'fitness/workout_timer.html', {'active_page': 'workout_timer'})


def gallery(request):
    context = {'active_page': 'gallery', 'gallery_images': data.GALLERY_IMAGES}
    return render(request, 'fitness/gallery.html', context)


def pricing(request):
    context = {'active_page': 'pricing', 'plans': data.PRICING_PLANS, 'faqs': data.FAQS[:4]}
    return render(request, 'fitness/pricing.html', context)


def testimonials(request):
    context = {'active_page': 'testimonials', 'testimonials': data.TESTIMONIALS}
    return render(request, 'fitness/testimonials.html', context)


def faq(request):
    context = {'active_page': 'faq', 'faqs': data.FAQS}
    return render(request, 'fitness/faq.html', context)


def blog(request):
    context = {'active_page': 'blog', 'posts': data.BLOG_POSTS}
    return render(request, 'fitness/blog.html', context)

@login_required(login_url='login')
def contact(request):
    return render(request, 'fitness/contact.html', {'active_page': 'contact'})

def signup_view(request):
    return render(request, 'fitness/signup.html', {'active_page': 'signup'})

@login_required(login_url='login')
def free_trial(request):
    return render(request, 'fitness/free_trial.html', {'active_page': 'free_trial'})

@login_required(login_url='login')
def contact(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()
        subject = request.POST.get("subject", "").strip()

        
        if not name or not email or not phone or not subject or not message:
            messages.error(
                request,
                "Please fill in all the required fields."
            )
            return redirect("contact")

        
        if not phone.isdigit() or len(phone) != 10:
            messages.error(
                request,
                "Phone number must contain exactly 10 digits."
            )
            return redirect("contact")

        
        email_body = f""" Name: {name} Email: {email} Phone: {phone} Subject: {subject} Message:{message} """

        
        email_message = EmailMessage(
            subject=f"IRONCORE Contact Message from {name}",
            body=email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.ADMIN_EMAIL],
            reply_to=[email],
        )

        
        email_message.send(fail_silently=False)

        
        messages.success(
            request,
            "Thank you! Your message has been sent successfully."
        )

        return redirect("contact")

    return render(
        request,
        "fitness/contact.html",
        {"active_page": "contact"}
    )


def error_404(request, exception=None):
    return render(request, 'fitness/404.html', status=404)

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        errors = []
        if not username:
            errors.append("Username is required.")

        if not email:
            errors.append("Email is required.")

        if not password1:
            errors.append("Password is required.")

        if username and User.objects.filter(username__iexact=username).exists():
            errors.append("Username already exists.")

        if email and User.objects.filter(email__iexact=email).exists():
            errors.append("Email already exists.")

        if password1 and password2:
            if password1 != password2:
                errors.append("Passwords do not match.")

            elif len(password1) < 8:
                errors.append(
                    "Password must contain at least 8 characters."
                )

        if errors:
            return render(
                request,
                "fitness/register.html",
                {
                    "errors": errors,
                    "username": username,
                    "email": email,
                }
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(
            request,
            "Account created successfully. Please login."
        )

        return redirect("login")

    return render(request, "fitness/register.html")


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if not email or not password:
            return render(
                request,
                "fitness/login.html",
                {
                    "error": "Email and password are required.",
                    "email": email,
                }
            )

       
        try:
            user_obj = User.objects.get(
                email__iexact=email
            )
        except User.DoesNotExist:

            return render(
                request,
                "fitness/login.html",
                {
                    "error": "Invalid email or password.",
                    "email": email,
                }
            )

       
        user = authenticate(
            request,
            username=user_obj.username,
            password=password
        )

        if user is not None:

            login(request, user)

            
            next_url = (
                request.POST.get("next")
                or request.GET.get("next")
            )

            if next_url:
                return redirect(next_url)

            return redirect("home")

        return render(
            request,
            "fitness/login.html",
            {
                "error": "Invalid email or password.",
                "email": email,
            }
        )

    return render(request, "fitness/login.html")

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def payment(request, plan_id):
    return render(request, "fitness/payment.html", {
        "plan_id": plan_id
    })
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("home")

@login_required(login_url='login')
def profile(request):

    return render(
        request,
        "fitness/profile.html",
        {
            "user": request.user
        }
    )

@login_required(login_url='login')
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Your password has been changed successfully."
            )

            return redirect("profile")

    else:

        form = PasswordChangeForm(
            request.user
        )

    return render(
        request,
        "fitness/change_password.html",
        {
            "form": form
        }
    )

from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay


@login_required(login_url="login")
def payment(request, plan_id):

    plans = {
        1: {"name": "Basic", "price": 1499},
        2: {"name": "Pro", "price": 2999},
        3: {"name": "Elite", "price": 4999},
    }

    plan = plans.get(plan_id)

    
    if not plan:
        return redirect("pricing")

    
    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    
    order = client.order.create({
        "amount": plan["price"] * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    print("Plan ID:", plan_id)
    print("Plan:", plan)
    print("Razorpay Order:", order)

    context = {
        "plan": plan,
        "plan_id": plan_id,
        "order": order,
        "razorpay_key_id": settings.RAZORPAY_KEY_ID,
    }

    return render(
        request,
        "fitness/payment.html",
        context
    )

import json
import requests
import os

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

N8N_WEBHOOK = os.getenv('N8N_WEBHOOK', '')


def chatbox(request):
    return render(request, "fitness/chatbox.html")


@csrf_exempt
def ai_chat(request):

    if request.method == "POST":

        data = json.loads(request.body)
        print(data)

        message = data.get("message")
        level = data.get("level")
        file = data.get("file")
        filename = data.get("filename")
        mimetype = data.get("mimetype")

        response = requests.post(
            N8N_WEBHOOK,
            json={
                "message": message,
                "level": level,
                "file": file,
                "filename": filename,
                "mimetype": mimetype
            }
        )

        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        if response.status_code == 200:
            try:
                return JsonResponse(response.json())
            except Exception as e:
                return JsonResponse({
                    "reply": response.text,
                    "error": str(e)
                })

        return JsonResponse({
            "reply": "Sorry, AI is unavailable."
        })
@login_required(login_url='login')
def chest_exercises(request):
    from .data import CHEST_EXERCISES

    return render(
        request,
        "fitness/chest_exercises.html",
        {
            "exercises": CHEST_EXERCISES
        }
    )
@login_required(login_url='login')
def back_exercises(request):
    from .data import BACK_EXERCISES

    return render(
        request,
        "fitness/back_exercises.html",
        {
            "exercises": BACK_EXERCISES
        }
    )
@login_required(login_url='login')
def legs_exercises(request):
    from .data import LEGS_EXERCISES

    return render(
        request,
        "fitness/legs_exercises.html",
        {
            "exercises": LEGS_EXERCISES
        }
    )
@login_required(login_url='login')
def shoulders_exercises(request):
    from .data import SHOULDERS_EXERCISES

    return render(
        request,
        "fitness/shoulders_exercises.html",
        {
            "exercises": SHOULDERS_EXERCISES
        }
    )
@login_required(login_url='login')
def arms_exercises(request):
    from .data import ARMS_EXERCISES

    return render(
        request,
        "fitness/arms_exercises.html",
        {
            "exercises": ARMS_EXERCISES
        }
    )
@login_required(login_url='login')
def core_exercises(request):
    from .data import CORE_EXERCISES

    return render(
        request,
        "fitness/core_exercises.html",
        {
            "exercises": CORE_EXERCISES
        }
    )
@login_required(login_url='login')
def cardio_exercises(request):
    from .data import CARDIO_EXERCISES

    return render(
        request,
        "fitness/cardio_exercises.html",
        {
            "exercises": CARDIO_EXERCISES
        }
    )
@login_required(login_url='login')
def fullbody_exercises(request):
    from .data import FULLBODY_EXERCISES

    return render(
        request,
        "fitness/fullbody_exercises.html",
        {
            "exercises": FULLBODY_EXERCISES
        }
    )


def blog(request):
    context = {
        'active_page': 'blog',
        'posts': data.BLOG_POSTS,
    }
    return render(request, "fitness/blog.html", context)

@login_required(login_url='login')
def blog_detail(request, slug):
    post = next((p for p in data.BLOG_POSTS if p["slug"] == slug), None)
    if post is None:
        from django.http import Http404
        raise Http404("Blog post not found")
    return render(request, "fitness/blog-detail.html", {"post": post})
