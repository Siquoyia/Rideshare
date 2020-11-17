from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RideShare
from .forms import RideShareForm
from rideshare import views as rideshare_views


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
                  {"rideshares": rideshares, 'form':form})

def add_rideshare(request):               
    if request.method == 'GET':
        form = RideShareForm()
    else:
        form = RideShareForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='booked_rideshare')

    return render(request, "rideshare/add_rideshare.html", {"form": form})


    

#def list_rideshares(request):
    #if request.method == 'GET':
        #form = RideShareForm()
        #return render(request, "list_rideshares.html", {"form": form})



#class RideData(rideshare_views):
    #template_name = 'rideshares/list_rideshares.html'
    #model = RideShare
    #success_url = list_rideshares('rideshares:rideshares')


def booked_ride(request):
    return render(request, "rideshare/booked_rideshare.html")