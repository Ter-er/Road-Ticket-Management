from django.db import models

# Create your models here.

class User(models.Model):
    USER_ROLES = (
        ('motorist', 'Motorist'),
        ('admin', 'Admin'),
        ('official', 'Official'),
    )
    
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True, null=True)  # Optional middle/other name
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    license_no = models.CharField(max_length=20, unique=True)
    #password_hash = models.CharField(max_length=128)  # Store the hashed password here
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.license_no}"