from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ReliefCenter(models.Model):
    contact = models.CharField(max_length=10)
    location = models.TextField()
    donation_received = models.PositiveIntegerField()
    type_of_disaster = models.CharField(max_length=100)
