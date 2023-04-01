from django.contrib import admin
from .models import Elevator

# Register your models here.

class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('id','up', 'down', 'open','close', 'running','stop')
admin.site.register(Elevator, ElevatorAdmin)
