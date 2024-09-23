from typing import Any
from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from .models import User

class EmailLicenseNoBackend(BaseBackend):
    def authenticate(self, request, email=None, license_no=None):
        try:
            user = User.objects.get(email=email, license_no=license_no, role='motorist')
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        

class OfficialEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username, role='official')
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None