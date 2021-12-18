# 17
import time
import numpy as np
from enum import Enum

debug = True
# sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()

# Loading
lines = open("input.txt", 'r').read().splitlines()

_, target_str = lines[0].split(": ")
x_str, y_str = target_str.split(", ")
x_vals = x_str[2:].split("..")
y_vals = y_str[2:].split("..")
x_range = [int(i) for i in x_vals]
y_range = [int(i) for i in y_vals]
target = [x_range, y_range]
# debug_log(x_range, y_range)

class Location(Enum):
    IN_TARGET = 0
    CONTINUE = 1
    UNDER = 2
    TOO_FAR = 3
    NOT_FAR_ENOUGH = 4

def where_am_i(pos, target_ranges):
    left = target_ranges[0][0]
    right = target_ranges[0][1]
    bottom = target_ranges[1][0]
    top = target_ranges[1][1]
    location = None
    if pos[1] >= top or (pos[1] >= bottom and pos[0] <= left):
        location = Location.CONTINUE
    # elif pos[0] >= left and pos[0] <= right and pos[1] >= top:
    #     location = Location.CONTINUE
    elif left <= pos[0] <= right and bottom <= pos[1] <= top:
        location = Location.IN_TARGET
    elif  left <= pos[0] <= right and pos[1] <= bottom:
        location = Location.UNDER
    elif pos[0] >= right:
        location = Location.TOO_FAR
    elif pos[0] <= left and pos[1] <= bottom:
        location = Location.NOT_FAR_ENOUGH
    else: 
        location = Location.CONTINUE
    # raise ValueError("Impossible value of Location!")
    
    return location

def next_step(pos, velocity, target_ranges):
    new_pos = [pos[0]+velocity[0], pos[1]+velocity[1]]
    new_velocity = velocity
    if velocity[0] > 0: new_velocity[0] -= 1
    elif velocity[0] < 0:               new_velocity[0] += 1
    new_velocity[1] -= 1

    location = where_am_i(new_pos, target_ranges)

    status = 0
    if (location == Location.NOT_FAR_ENOUGH or 
        location == Location.TOO_FAR or 
        location == Location.UNDER):
        status = -1
    elif location == Location.CONTINUE:
        status = 0
    elif location == Location.IN_TARGET:
        status = 1
        

    return new_pos, new_velocity, status

start = [0,0]

print(where_am_i(start, target))

valid_velocities =[]
best_y = -1
best_start_vel = [-1,-1]
last_tested = [-1,-1]
total_valid = 0
# try:
for i in range(0, 310):
    for j in range(-300, 401):
        if j%50 ==0: print(f"Tested up to [{i,j}]")
        last_tested = [i,j]
        pos = start.copy()
        start_vel = [i,j]
        vel = start_vel.copy()
        status = 0
        apogee = -1
        while status == 0:
            pos, vel, status = next_step(pos, vel, target)
            # if vel[1] == 0:
            #     apogee = pos[1]
            if vel[0] == 0 and pos[0] < target[0][0]:
                continue
        if status == 1:
            total_valid += 1
            # valid_velocities.append([start_vel,apogee])
            # if apogee > best_y:
            #     best_y = apogee
            #     best_start_vel = start_vel

# except ValueError as e:
#     print(e)
print(f"Best velocity = {best_start_vel}, apogee = {best_y}") # 3570 
print(f"Valid velocities = {total_valid}, Time={time.time() - startTime}s")
# 1845 too low

with open("output_velocities_complete.txt","w") as f:
    for i in valid_velocities:
        f.write(f" [{i[0][0]},{i[0][1]}] => y={i[1]}\n")
    
    

print("Done")