from django.db import models

from hotel_shared.models import HotelType


# Create your models here.
class Hotel(models.Model):
    hotel_type = models.ForeignKey(HotelType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    available_rooms = models.IntegerField()

    def __str__(self):
        return self.name
