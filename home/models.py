from django.db import models

# Create your models here.

class Elevator(models.Model):
    id = models.IntegerField(primary_key=True)
    up = models.BooleanField(default=False)
    down = models.BooleanField(default=False)
    running = models.BooleanField(default=False)
    stop = models.BooleanField(default=True)
    open = models.BooleanField(default=False)
    close = models.BooleanField(default=True)

    def __str__(self):
        return self.id
   

