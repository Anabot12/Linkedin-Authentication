# accounts/views.py

from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class LinkedInLogin(SocialLoginView):
    adapter_class = LinkedInOAuth2Adapter
