from django.db import models
from customers.models import Customer
# Create your models here.




class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(choices=REQUEST_TYPES, max_length=50)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} from {self.customer.first_name} {self.customer.last_name}"