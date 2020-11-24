from django import forms
from .models import RideShare, Passenger, Driver, Destination


class RideShareForm(forms.ModelForm):
    class Meta:
        model = RideShare
        fields = [
            'passenger',
            'number_of_passengers',
            'driver',
            'destination',
            'date_and_time',
            'phone_number',
        ]

#class PassengerForm(forms.ModelForm):
    #class Meta:
        #model = Passenger
        #fields = [
            #'date_and_time',
        #]