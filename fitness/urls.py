
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import (
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView
)
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('workout-plans/', views.workout_plans, name='workout_plans'),
    path('diet-plans/', views.diet_plans, name='diet_plans'),
    path('trainers/', views.trainers, name='trainers'),
    path('bmi-calculator/', views.bmi_calculator, name='bmi_calculator'),
    path('calorie-calculator/', views.calorie_calculator, name='calorie_calculator'),
    path('workout-timer/', views.workout_timer, name='workout_timer'),
    path('gallery/', views.gallery, name='gallery'),
    path('pricing/', views.pricing, name='pricing'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path(
        'payment/<int:plan_id>/',
        views.payment,
        name='payment'
    ),

    path('logout/', views.logout_view, name='logout'),

    path('chatbox/', views.chatbox, name='chatbox'),
    path('ai-chat/', views.ai_chat, name='ai_chat'),


    path(
        'chest-exercises/',
        views.chest_exercises,
        name='chest_exercises'
    ),
    path(
        'back-exercises/',
        views.back_exercises,
        name='back_exercises'
    ),
    
    path(
        'legs-exercises/',
        views.legs_exercises,
        name='legs_exercises'
    ),
    path(
        'shoulders-exercises/',
        views.shoulders_exercises,
        name='shoulders_exercises'
    ),
    path(
        'arms-exercises/',
        views.arms_exercises,
        name='arms_exercises'
    ),
    path(
        'core-exercises/',
        views.core_exercises,
        name='core_exercises'
    ),
    path(
        'cardio-exercises/',
        views.cardio_exercises,
        name='cardio_exercises'
    ),
    path(
        'fullbody-exercises/',
        views.fullbody_exercises,
        name='fullbody_exercises'
    ),
    path(
    'blog/', views.blog, name='blog'),
    path(
    'blog/<slug:slug>/', views.blog_detail, name='blog_detail'
    ),


    path(
    'forgot-password/',
    auth_views.PasswordResetView.as_view(
        template_name='fitness/password_reset.html',
        email_template_name='fitness/password_reset_email.html',
        success_url='/forgot-password/sent/'
    ),
    name='password_reset'
    ),

path(
    'forgot-password/sent/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='fitness/password_reset_done.html'
    ),
    name='password_reset_done'
),

path(
    'reset-password/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='fitness/password_reset_confirm.html',
        success_url='/reset-password/complete/'
    ),
    name='password_reset_confirm'
),

path(
    'reset-password/complete/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='fitness/password_reset_complete.html'
    ),
    name='password_reset_complete'
),
path(
    'profile/',
    views.profile,
    name='profile'
),
path(
    'change-password/',
    PasswordChangeView.as_view(
        template_name='fitness/change_password.html',
        success_url='/change-password/done/'
    ),
    name='change_password'
),

path(
    'change-password/done/',
    PasswordChangeDoneView.as_view(
        template_name='fitness/change_password_done.html'
    ),
    name='change_password_done'
),

]