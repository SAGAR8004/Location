from os import name
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from geopy import Nominatim, location
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Sagar'})

def add(request):

    lat = float(request.GET["lat"])
    long = float(request.GET["long"])

    geolocator= Nominatim(user_agent= 'test/1')
    location = geolocator.reverse((lat, long))
    print(location.address)

    # location = lat+long

    return render(request, 'base.html', {'location': location.address})