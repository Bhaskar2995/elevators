from .models import Elevator
import time
from celery import shared_task
from django.http import JsonResponse

elevator_dict = {}

@shared_task
def state_elevator(id,state):
    elevator = Elevator.objects.get(id=id)
    if state == 'open':
        if elevator.state == 'open':
            return JsonResponse({'error':'elevator is already opened'})
        elevator.state = "opening"
        elevator.save()
        time.sleep(10)
        elevator.state = "closing"
        elevator.save()
        time.sleep(10)
        elevator.state = "closed"
        elevator.save()
    else:
        if elevator.state == "closed":
            return JsonResponse({'error':'Elevator is already closed'})
        elevator.state = "closing"
        elevator.save()
        time.sleep(10)
        elevator.state = "closed"
        elevator.save()
    return JsonResponse({'id':elevator.id,'Present Floor': elevator.floor, 'state':elevator.state})


@shared_task
def assign_elevator(floor):
    elevators = Elevator.objects.exclude(maintenance= True).order_by('floor')
    min_value = float('inf')
    for elevator in elevators:
        if not elevator.status == "running":
            value = abs(floor - elevator.floor)
            if value < min_value:
                min_value = value
                closest_elevator = elevator
                closest_elevator.status = "running"
                closest_elevator.next_destination = floor

    if closest_elevator.id not in elevator_dict:
        elevator_dict[closest_elevator.id] = closest_elevator.status
    movement = floor - closest_elevator.floor
       
    if movement < 0:
        closest_elevator.direction = "down"   
    else:
        closest_elevator.direction = "up"
    closest_elevator.save()
    time.sleep(abs(movement))
    closest_elevator.floor = floor
    closest_elevator.direction = "None"
    closest_elevator.status = "stop"
    closest_elevator.next_destination = 0
    closest_elevator.state = "opening"
    closest_elevator.save()
    time.sleep(10)
    closest_elevator.state = "open"
    closest_elevator.save()
    time.sleep(10)
    closest_elevator.state = "closing"
    closest_elevator.save()
    time.sleep(10)
    closest_elevator.state = "closed"
    closest_elevator.save()

    