from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RideShare
from .forms import RideShareForm


# Create your views here.

def home(request):
    rideshares = RideShare.objects.all()
    if request.method == 'GET':
        form = RideShareForm()
    else:
        form = RideShareForm(data=request.POST)
        if form.is_valid():
            form.save()        
   
    return render(request, "rideshare/home.html",
                  {"rideshares": rideshares})

def add_rideshare(request):               
    if request.method == 'GET':
        form = RideShareForm()
    else:
        form = RideShareForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')

    return render(request, "rideshare/home.html", {"form": form})

