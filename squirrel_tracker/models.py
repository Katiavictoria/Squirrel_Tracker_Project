from django.db import models



class Sightings(models.Model):
    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    Unique_Squirrel_ID = models.CharField(max_length=50)
    Shift = models.CharField(max_length=50)
    Date = models.DateField(null=True)
    Age = models.CharField(max_length=50)
    Primary_Fur_Color = models.CharField(max_length=70)
    Location  = models.CharField(max_length=100)
    Specific_Location  = models.CharField(max_length=100)
    Running = models.BooleanField(null=True)
    Chasing = models.BooleanField(null=True)
    Climbing = models.BooleanField(null=True)
    Eating = models.BooleanField(null=True)
    Foraging = models.BooleanField(null=True)
    Other_Activities = models.CharField(max_length=100)
    Kuks = models.BooleanField(null=True)
    Quaas = models.BooleanField(null=True)
    Moans = models.BooleanField(null=True)
    Tail_Flags = models.BooleanField(null=True)
    Tail_Twitches = models.BooleanField(null=True)
    Approaches = models.BooleanField(null=True)
    Indifferent = models.BooleanField(null=True)
    Runs_From = models.BooleanField(null=True)


def _str_(self):
    return self.Unique_Squirrel_ID
