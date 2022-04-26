from django.shortcuts import render
from django.http import HttpResponse
from .forms import Address
from .models import Place

# Create your views here.

def loc(request):
    form = Address()
    place = Place.objects.last().location
    print(type(place))
    place = place.split(",")
    print(place[0])

    # print(resaneh.location)
    context ={
    "form" : form,
    "place":place,

    }
    return render(request, "location/main.html", context)
    # return render(request, "home/faq.html")
