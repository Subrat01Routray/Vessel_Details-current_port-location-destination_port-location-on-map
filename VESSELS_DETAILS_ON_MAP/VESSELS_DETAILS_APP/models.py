from django.db import models

class RouteDetails(models.Model):
    vessel_number = models.CharField(primary_key=True, max_length=100)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    current_port = models.CharField(max_length=100)
    current_port_latitude = models.FloatField()
    current_port_longitude = models.FloatField()
    destination_port = models.CharField(max_length=100)
    destination_port_latitude = models.FloatField()
    destination_port_longitude = models.FloatField()