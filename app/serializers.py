from rest_framework import serializers
from .models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['temperature', 'humanlity', 'soilMoisture' , 'watering', 'time']
