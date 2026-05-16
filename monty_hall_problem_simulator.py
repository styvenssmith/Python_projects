'''
Problem:
you pick door 1
host reveals a goat behind door 3
should you switch
we simulate 100,000 trials for both strategies
to verify 2/3 and 1/3 split analytically
'''


import numpy as np
import random

#keeps track of wins if we stay
stay = 0
#keeps track of wins if we move
switch = 0
for i in range(1, 100000+1):
    #choosing the destination for the car
    car = random.randint(1,3)
    #we choose door 1
    pick = 1
    #monty opens a door that does not include the car, and is not the door we chose
    monty = [door for door in [1,2,3] if door!=car and door!=pick][0]
    #if we do decide to switch, this is the door we are switching to
    _switch = [door for door in [1,2,3] if door !=monty and door!=pick][0]
    
    if pick==car:
        stay = stay+1
    if _switch==car:
        switch = switch+1
     
        
print(f"Win given stay = {stay/100000}")
print(f"Win given switch = {switch/100000}")
