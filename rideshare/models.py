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
    driver = models.ForeignKey("Driver",on_delete=models.CASCADE, related_name="rideshares")
    date_and_time = models.DateTimeField(default=datetime.now)
    is_complete = models.BooleanField(default=False)
    number_of_passengers = models.CharField(max_length=1,choices=PASSENGER_CHOICES)
    destination = models.ForeignKey("Destination",on_delete=models.CASCADE,related_name="rideshares")

class Destination(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    address = models.TextField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.address   
    
class Passenger(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    address = models.TextField(max_length=255,null=True, blank=True)
    #date_and_time =models.TextField(max_length=255,null=True, blank=True)
    
    def __str__(self):
        return self.name 

class Driver(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    vehicle_description = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name