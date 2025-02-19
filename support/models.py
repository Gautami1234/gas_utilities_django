from django.db import models
from requests.models import ServiceRequest

class SupportTicket(models.Model):
     service_request = models.TextField()
     assigned_at = models.DateTimeField(auto_now_add=True)
     STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
     ]
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
     resolution_notes = models.TextField(blank=True, null=True)

     def __str__(self):
        return f"Ticket {self.id} - {self.status}"


