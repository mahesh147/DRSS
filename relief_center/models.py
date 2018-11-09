from django.db import models


class ReliefCenter(models.Model):
    contact_no = models.IntegerField()
    location = models.TextField()
    donation_received = models.IntegerField()
    type_of_disaster = models.CharField(max_length=100)
