from datetime import datetime
from django.db import models

# Create your models here.
class Sensordata(models.Model):
    temperature = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_direction = models.IntegerField()
    precipitation = models.IntegerField()
    current = models.IntegerField()
    power = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)