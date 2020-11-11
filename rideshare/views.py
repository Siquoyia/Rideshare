from django.shortcuts import render
from django.http import HttpResponse
from .models import RideShare

# Create your views here.

def home(request):
    rideshares = RideShare.objects.all()
    return render(request, "rideshare/list_rideshares.html",
                  {"rideshares": rideshares})


