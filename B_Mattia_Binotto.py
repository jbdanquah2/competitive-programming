from collections import deque

def detNotDisappointedDrivers(n, t):

    if n == 0:  
        return 0

    queue = deque(t)  
    queue = deque(sorted(queue))  
    total_sum = 0  
    happyDrivers = 0 
 
    for driver in queue:
        if total_sum <= driver:
            happyDrivers += 1 
        total_sum += driver

    return happyDrivers

n = int(input())  # Number of drivers
t = list(map(int, input().split()))  # List of times for each driver

print(detNotDisappointedDrivers(n, t))
