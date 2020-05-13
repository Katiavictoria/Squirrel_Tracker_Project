from django.shortcuts import render, redirect
from .models import Sightings
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Count

from django.http import HttpResponse

def sightings(request):
    all_sightings = Sightings.objects.all()
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'sightings.html',context)

def map(request):
    all_sightings = Sightings.objects.all()[:100]
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'map.html',context)
