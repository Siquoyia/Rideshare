from django import forms
from .models import RideShare, Passenger, Driver


class RideShareForm(forms.ModelForm):
    class Meta:
        model = RideShare
        fields = [
            'passenger',
            'number_of_passengers',
            'driver',
            'destination',
        ]

#class NoteForm(forms.ModelForm):
     #class Meta:
         #model = Note
         #fields = [
             #'text',
         #]