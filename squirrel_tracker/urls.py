from django.urls import path 

from . import views

urlpatterns = [
    path('sightings/', views.sightings),
    path('map/',views.map),
    path('sightings/statistics/', views.sightings_statistics),
    path('sightings/add/', views.sightings_add, name='add'),
    path('sightings/<Unique_Squirrel_ID>/', views.sightings_update, name='update'),
    ]
