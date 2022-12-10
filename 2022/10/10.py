# day 10

import numpy as np
from copy import deepcopy


sample = False
# sample = True
debug = False
# debug = True



if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

def is_interest(cycle):
    first_interest = 20
    period = 40
    if cycle >= 240:
        return False
    if cycle < first_interest:
        return False
    elif (cycle - first_interest) % period == 0:
        return True
    else:
        return False
    
screen = ["" for i in range(6)]

def pixel(cycle, pos):
    period = 40
    max = 240
    if cycle >= max : 
        return
    x_pos = cycle % period
    y_pos = (cycle-1) // period
    if debug: print("Drawing pixel: ", (y_pos, x_pos))
    if pos-1 <= x_pos-1 <= pos +1:
        screen[y_pos] += "#"
    else: 
        screen[y_pos] += "."



clock = 0
reg = 1
max = 240
interests = []

for l in lines:
    op = l.split(" ")
    if op[0] == "noop":
        clock += 1
        pixel(clock, reg)
        if is_interest(clock):
            interests.append(reg*clock)
    else: 
        assert(op[0] == "addx")
        clock += 1
        if debug: print(clock, reg)
        pixel(clock, reg)
        if is_interest(clock):
            interests.append(reg*clock)
        clock += 1
        if debug: print(clock, reg)
        if is_interest(clock):
            interests.append(reg*clock)
        pixel(clock, reg)
        reg += int(op[1])
    if clock >= max:
        break

print(interests)
print("Part 1:", sum(interests) )
print("Part 2:" )
for i in screen:
    print(i)
