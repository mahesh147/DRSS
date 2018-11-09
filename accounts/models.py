from django.db import models


class Account(models.Model):
    contact_number = models.IntegerField()
    email_id = models.EmailField()
