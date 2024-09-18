from django.db import models

# Create your models here.

class Vehicle(models.Model):
    owner = models.ForeignKey('User.User', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=15, unique=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    license_issue_date = models.DateField()
    license_expiry_date = models.DateField()

    def __str__(self):
        return f"{self.make} {self.model} {self.plate_number}"