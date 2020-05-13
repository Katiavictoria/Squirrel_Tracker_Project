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

def sightings_statistics(request):
    all_sightings = Sightings.objects.all()
    squirrel_age = Sightings.objects.values('Age').order_by('Age').annotate(age_count=Count('Age'))
    squirrel_primary_fur_color = Sightings.objects.values('Primary_Fur_Color').order_by('Primary_Fur_Color').annotate(primaryfurcolor_count=Count('Primary_Fur_Color'))
    squirrel_kuks =  Sightings.objects.values('Kuks').order_by('Kuks').annotate(climbing_count=Count('Kuks'))
    squirrel_quaas = Sightings.objects.values('Quaas').order_by('Quaas').annotate(chasing_count=Count('Quaas'))
    squirrel_moans = Sightings.objects.values('Moans').order_by('Moans').annotate(running_count=Count('Moans'))
    context = {
        'squirrel_age': squirrel_age,
        'squirrel_primary_fur_color': squirrel_primary_fur_color,
        'squirrel_kuks': squirrel_kuks,
        'squirrel_quaas': squirrel_quaas,
        'squirrel_moans': squirrel_moans,
    }
    return render(request, 'statistics.html', context)
