ELEVATOR SYSTEM

I have designed a Elevator system which consists of N elevators. It does following operations:

1) Takes the floor number from the user

2) Assigns the nearest elevator to the user

3) Displays the status (running or stopped), direction (moving up/down), state (openned, closed, opening, closing)

Libraries Used:

1) Python (3.10.5)

2) Django (4.1.7)

3) Redis (4.5.4)

4) Celery (5.2.7)

API's USED

1) Initialise the elevator system to create ‘n’ elevators in the system (Say we are initiazing with 5 elevators)

API CALL: http://localhost:8000/initialize/5

OUTPUT: {"success": "Initialized with 5 elevators"}

2) Takes user input for floor number to attend (Let the user call is for 14th floor)

API CALL: http://localhost:8000/floor/14

OUPUT: {"success": "closest elevator is assigned"}

3) Fetch all information related to a given elevator (If 2nd Elevator takes the call)

API CALL: http://localhost:8000/request/2 

OUTPUT: {"id": 2, "status": "running", "Present Floor": 0, "Direction": "up", "Next Destination": 14}

Here we can see the direction (moving up/down), status (running,stopped), next destination floor

4) Fetch the next destination floor for a given elevator (Or seperately see only the next destination floor of a particular elevator)

API CALL: http://localhost:8000/next/2

OUTPUT: {"Next Destination": 14}

5) Mark a elevator as not working or in maintenance (Say we are marking elevator 5 as not working)

API CALL: http://localhost:8000/maintenance/5

OUTPUT: {"success": "Elevator 5 is in maintenance"}

Now Elevator 5 will not be assigned to any user till maintenance is done

6) Open/close the door

API CALL: http://localhost:8000/state/2/open 

OUTPUT: {"id": 2, "status": "stop", "Present Floor": 14, "state": "opening"}

It checks if the status is in "stop" and opens or closes the door of the elevator

Example output in Django admin

![Select elevator to change _ Django site admin - Google Chrome 4_2_2023 1_55_59 PM](https://user-images.githubusercontent.com/98119194/229341767-24522b7b-c9d9-419c-9829-74eab398a3b8.png)

