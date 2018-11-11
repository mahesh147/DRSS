from django.db import models
from relief_center.models import ReliefCenter


class WantedItem(models.Model):
    item_name = models.CharField(max_length=200)
    urgency_level = models.SmallIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    relief_center_id = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.item_name
