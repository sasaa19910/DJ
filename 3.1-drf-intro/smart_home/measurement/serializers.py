from rest_framework import serializers
from .models import Sensor, Measurement



class SensorSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSeralizer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'sensor_id', 'create_at', '']

class SensorDetaliSeralizer(serializers.ModelSerializer):
    measurements = MeasurementSeralizer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

