from django.db import models





class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()



class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor,on_delete=models.CASCADE)
    temperature = models.FloatField()
    create_at = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)











