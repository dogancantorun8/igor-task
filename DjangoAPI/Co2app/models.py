from django.db import models

# Create your models here.

class Analytics(models.Model): 
        id=models.AutoField(primary_key=True) 
        shipment_id=models.FloatField() 
        weight_kg =models.FloatField()  
        distance_km =models.FloatField()  
        pickup_time = models.DateTimeField()
        dropoff_time = models.DateTimeField()
        
