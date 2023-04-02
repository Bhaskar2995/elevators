from django.db import models

# Create your models here.

class Elevator(models.Model):
    STATUS_CHOICES = [
        ('running','running'),
        ('stop','stop')
    ]
    DIRECTION_CHOICES = [
        ('up','up'),
        ('down','down')
    ]
    id = models.IntegerField(primary_key=True)
    direction = models.CharField(choices=DIRECTION_CHOICES,max_length=100,default='None')
    status = models.CharField(choices=STATUS_CHOICES, max_length=100, default = "stop")
    open = models.BooleanField(default=False)
    close = models.BooleanField(default=True)
    maintenance = models.BooleanField(default=False)
    floor = models.IntegerField(default=0)
    next_destination = models.IntegerField(default=0)
    state = models.CharField(max_length=300,default="closed")
   

