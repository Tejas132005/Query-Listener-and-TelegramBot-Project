from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):  
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('postponed', 'Postponed'),
        ('resolved', 'Resolved'),
    ]
    TYPE_CHOICES = [
        ('query', 'Query'),
        ('complaint', 'Complaint'),
        ('feedback', 'Feedback'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')  # ✅ Fixed
    admin_response = models.TextField(blank=True, null=True)  # ✅ Added
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            import random
            self.ticket_number = f"TKT{random.randint(10000, 99999)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_number} - {self.title}"
