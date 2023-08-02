# accounts/urls.py

from django.urls import path
from .views import LinkedInLogin

urlpatterns = [
    # ...
    path('accounts/linkedin/', LinkedInLogin.as_view(), name='linkedin_login'),
    # Add more URL patterns for other views (e.g., registration, login, logout)
    # ...
]
