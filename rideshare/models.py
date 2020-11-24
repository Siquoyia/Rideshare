from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator






# Create your models here.
class RideShare(models.Model):

    passenger = models.ForeignKey("Passenger",on_delete=models.CASCADE,related_name="rideshares")
    driver = models.ForeignKey("Driver",on_delete=models.CASCADE, related_name="rideshares")
    date_and_time = models.DateTimeField(default=datetime.now)
    is_complete = models.BooleanField(default=False)
    number_of_passengers = models.PositiveIntegerField(validators=[MaxValueValidator(3)])
    destination = models.ForeignKey("Destination",on_delete=models.CASCADE,related_name="rideshares")
    phone_number = models.CharField(max_length=255,null=True, blank=True)

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
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.name