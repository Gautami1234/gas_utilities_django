from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer, name='register_customer'),
    path('success/', views.registration_success, name='registration_success'),
]
