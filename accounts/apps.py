# accounts/apps.py

from django.apps import AppConfig

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'  # Make sure this matches the correct app label 'account'
