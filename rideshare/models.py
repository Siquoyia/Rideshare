from datetime import datetime
from django.db import models


PASSENGER_CHOICES = (
  (1,1),
  (2,2),
  (3,3),
)  




# Create your models here.
class RideShare(models.Model):

    passenger = models.ForeignKey("Passenger",on_delete=models.CASCADE,related_name="rideshares")
    driver = models.ForeignKey(max_length=255,null=True, blank=True)
    schedule = models.DateTimeField(default=datetime.now)
    is_complete = models.BooleanField(default=False)
    number_of_passengers = models.ChoiceField(choices=PASSENGER_CHOICES)
    destination = models.ForeignKey("Destination",on_delete=models.CASCADE,related_name="rideshares")

class Destination(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    address = models.TextField(max_length=255,null=True, blank=True)
    link = models.UrlField()    
    
class Passenger(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    address = models.TextField(max_length=255,null=True, blank=True)

class Driver(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    vehicle_description = models.CharField(max_length=255,null=True, blank=True)