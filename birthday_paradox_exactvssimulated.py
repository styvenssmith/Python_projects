
'''
Birthday paradox
problem:
How many people are needed in a room for a 50%
chance of a shared birthday?
We will compute exact probability and simulate 50,000
groups of size n for n = 1 to 60
'''

import numpy as np
import random
import matplotlib.pyplot as plt


exact_arr = {}
def exact_solution(n):
    answer = 1.0
    for i in range(n):
        val = (365-i)/365
        answer = answer*val
        
    return 1-answer
        
for i in range(61):
    exact_arr[i] = exact_solution(i)
    
    
def n_choose_2(n):
    return (n*(n-1))//2


simulation = {}
def simulate_solution(n, runs = 25000):
    
    if n<2:
        return 0

    matches = 0
    for _ in range(runs):
        birthdays = [np.random.randint(1, 366) for _ in range(n)]
        #if number of unique birthdays is less than
        #the number of people we definitely have a match
        if(len(set(birthdays))<n):
            matches = matches+1
    simulation[n] = matches/runs
        
        
for i in range(1, 61):
    simulate_solution(i)
    
    
    
    
plt.plot(list(exact_arr.keys()), list(exact_arr.values()), label = 'exact solution')
plt.plot(list(simulation.keys()), list(simulation.values()), label ='simulation')
plt.xlabel('Total number of people')
plt.ylabel('Probability shared birthday')
plt.legend()
plt.show()