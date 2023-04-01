from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Elevator

# Create your views here.




class Index(View):
    def get(self,request,*args,**kwargs):
        elevators_to_initialize = kwargs['elevators']
        i=1
        while i<=elevators_to_initialize:
            elevator = Elevator(
                id = i                
            )
            elevator.save()
            i+=1
        return JsonResponse({'success':'Initialized with %s elevators' %elevators_to_initialize},status=200)
