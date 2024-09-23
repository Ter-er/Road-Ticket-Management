from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone 

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, license_no=None, role='motorist', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        # License number is required for motorists only
        if role == 'motorist' and not license_no:
            raise ValueError('Motorists must have a License Number')

        user = self.model(email=self.normalize_email(email), license_no=license_no, role=role, **extra_fields)

        # Handle password for officials (motorists don't use passwords)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user


class User(AbstractUser):
    USER_ROLES = (
        ('motorist', 'Motorist'),
        ('official', 'Official'),
    )
    
    username = models.CharField(max_length=100, unique=True, null=True)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True, null=True)  # Optional middle/other name
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    license_no = models.CharField(max_length=20, unique=True, blank=True, null=True)  # Optional for Admins and Officials
    date_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email} {self.license_no})"

    def is_motorist(self):
        return self.role == 'motorist'

    def is_official(self):
        return self.role == 'official'