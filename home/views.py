from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Elevator
from .helpers import assign_elevator
from threading import *

# Create your views here.

class Index(View):
    def get(self,request,*args,**kwargs):
        if 'elevators' in kwargs:
            # Initialize with n elevators
            elevators_to_initialize = kwargs['elevators']
            i=1
            Elevator.objects.all().delete()


            while i<=elevators_to_initialize:
                elevator = Elevator(
                    id = i                
                )
                elevator.save() 
                i+=1
            return JsonResponse({'success':'Initialized with %s elevators' %elevators_to_initialize},status=200)
        
        if 'maintenance' in kwargs:
            # Mark as not working for a particular elevator
            maintenance_elevator = kwargs['maintenance']
            elevator = Elevator.objects.get(id=maintenance_elevator)
            elevator.maintenance = True
            elevator.save()
            return JsonResponse({'success':'Elevator %s is in maintenance' %elevator.id},status=200)
        
        if 'user_request' in kwargs:
            user_request_list = []
            user_request_list.append(kwargs['user_request'])
            while(len(user_request_list)>0):
                assign_elevator.delay(kwargs['user_request'])
                user_request_list.pop(0)
            return JsonResponse({'success':'closest elevator is assigned'})

        if 'elevator_status' in kwargs:
            elevator = Elevator.objects.get(id=kwargs['elevator_status'])
            return JsonResponse({'Current Status':elevator.status})

