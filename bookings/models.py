from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('owner', 'Hotel Owner'),
        ('traveler', 'Traveler'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='traveler')

    def __str__(self):
        return f"{self.username} ({self.role})"



class Hotel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hotels")
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)  # Avg rating, auto-calculated
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"