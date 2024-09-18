from django.db import models

# Create your models here.

class Offense(models.Model):
    ticket_infringement = models.CharField(max_length=255)
    code = models.CharField(max_length=4)
    points = models.IntegerField()
    penalty = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
