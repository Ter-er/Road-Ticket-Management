from django.db import models
from User.models import User
from Vehicle.models import Vehicle
from Offense.models import Offense 

# Create your models here.

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    offense = models.ForeignKey(Offense, on_delete=models.CASCADE)
    ticket_image = models.ImageField(upload_to='ticket_images/', null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    official_name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    penalty = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ticket {self.id} - {self.vehicle.plate_number} - Offense: {self.offense.ticket_infringement} - Status: {self.status} - Penalty: ${self.penalty}"