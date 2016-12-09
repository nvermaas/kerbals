from django.db import models

class Kerbal(models.Model):
    name = models.CharField(max_length=50)
    trait = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    flights = models.IntegerField(default=0)
    land = models.CharField(max_length=255)
    orbit = models.CharField(max_length=255)
