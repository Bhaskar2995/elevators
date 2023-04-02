from django.contrib import admin
from .models import Elevator

# Register your models here.

class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('floor','id','status','direction','next_destination','state')
admin.site.register(Elevator, ElevatorAdmin)
