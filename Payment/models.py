from django.db import models
from datetime import timedelta
from django.utils import timezone
from Ticket.models import Ticket

# Create your models here.


class Payment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_deadline = models.DateTimeField(default=timezone.now() + timedelta(days=15))

    def __str__(self):
        return f"Payment {self.id} for Ticket {self.ticket.id}"