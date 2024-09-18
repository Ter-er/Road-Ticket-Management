from django.db import models
from Ticket.models import Ticket

# Create your models here.


class Proof(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    proof_date = models.DateTimeField(auto_now_add=True)
    proof_image = models.ImageField(upload_to='proof_images/', null=True, blank=True)  # Optional image field
    proof_video = models.FileField(upload_to='proof_videos/', null=True, blank=True)  # Optional video field
