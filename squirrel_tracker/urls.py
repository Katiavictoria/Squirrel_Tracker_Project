from django.urls import path 

from . import views

urlpatterns = [
    path('sightings/', views.sightings),
    path('map/',views.map),
    path('sightings/statistics/', views.sightings_statistics),
    ]
