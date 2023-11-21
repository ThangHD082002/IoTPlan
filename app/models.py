from django.db import models

# Create your models here.



class Sensor(models.Model):
    temperature = models.CharField(max_length=255)
    humanlity = models.CharField(max_length=255)
    soilMoisture = models.CharField(max_length=255)
    watering = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name
