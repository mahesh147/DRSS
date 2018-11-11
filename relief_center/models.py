from django.db import models
from django.contrib.auth.models import User


class ReliefCenter(models.Model):
    contact = models.CharField(max_length=10)
    location = models.TextField()
    donation_received = models.PositiveIntegerField()
    type_of_disaster = models.CharField(max_length=100)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, default='root')

    def __str__(self):
        return self.location
