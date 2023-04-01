from .models import Elevator
import time
from celery import shared_task

elevator_dict = {}

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
    closest_elevator.save()

    