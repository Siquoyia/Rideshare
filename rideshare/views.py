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
                  {"rideshares": rideshares, 'form':form})

def add_rideshare(request):               
    if request.method == 'GET':
        form = RideShareForm()
    else:
        form = RideShareForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')

    return render(request, "rideshare/home.html", {"form": form})


    

def delete_rideshare(request, pk):
    rideshare = get_object_or_404(RideShare, pk=pk)
    if request.method == 'POST':
        rideshare.delete()
        return redirect(to='list_rideshares')

    return render(request, "rideshares/delete_rideshare.html",
                  {"rideshare": rideshare})
