# 17
# second attempt at second part, based on
# https://www.reddit.com/r/adventofcode/comments/ri9kdq/comment/hozerr5/?utm_source=share&utm_medium=web2x&context=3

import time
from collections import defaultdict

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
x_range = sorted([int(i) for i in x_vals])
y_range = sorted([int(i) for i in y_vals])
target = [x_range, y_range]
# debug_log(x_range, y_range)

possible_xn = defaultdict(set)

for x in range(1, x_range[1]+1):
    n, xpos = 0, 0
    s = x
    while s > -200 and xpos <= x_range[1]:
        n+=1
        xpos += s if s>0 else 0
        s -= 1
        if x_range[0] <= xpos <= x_range[1]:
            possible_xn[n].add(x)
            

possible_yn = defaultdict(set)

for yspeed in range(y_range[0], 100):
    speed = yspeed
    ypos = n = 0
    while ypos >= y_range[0] and n<x_range[1]:
        n += 1
        ypos += speed
        speed -= 1
        if y_range[0] <= ypos <= y_range[1]:
            possible_yn[n].add(yspeed)

nboth = set(possible_xn.keys()).intersection(set(possible_yn.keys()))
pairs = {(x,y) for n in nboth for x in possible_xn[n] for y in possible_yn[n]}

print('p2',len(pairs))
