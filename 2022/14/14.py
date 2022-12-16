# day 14

import numpy as np
from copy import deepcopy

# sample = True
sample = False

if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()


max_w, max_h = 0, 0
min_w, min_h = 5000, 0

for l in lines:
    nums = l.split(" -> ")
    for pair in nums:
        l, r = pair.split(",")
        max_w = max(int(l), max_w)
        max_h = max(int(r), max_h)
        min_w = min(int(l), min_w)
        min_h = min(int(r), min_h)
max_w += (max_h - min_h) + 2
max_h += 3
min_w -= (max_h - min_h) +2
p_min = np.array([min_h, min_w])
p_max = np.array([max_h, max_w])
grid_size = p_max-p_min
print(p_min, p_max, grid_size)

grid = np.zeros(grid_size, dtype=np.int8)

def fill_in_rock(grid, text_line):
    nums = text_line.split(" -> ")
    points = []
    for pair in nums:
        y,x = (int(i) for i in pair.split(","))
        points.append(np.array([x,y]))
    for i in range(1,len(points)):
        p1 = points[i-1] - p_min
        p2 = points[i] - p_min
        if p1[0] == p2[0]:
            mn, mx = min(p1[1], p2[1]), max(p1[1], p2[1])
            for y in range(mn, mx+1):
                grid[p1[0], y] = 1
        elif p1[1] == p2[1]:
            mn, mx = min(p1[0], p2[0]), max(p1[0], p2[0])
            for x in range(mn, mx+1):
                grid[x, p1[1]] = 1
        else:
            raise Exception("Wrong set of rocks?")
for l in lines:
    fill_in_rock(grid, l)

p_spawn = np.array([0,500])-p_min
grid[tuple(p_spawn)] = 3
print(grid)

falling_forever = False
while not falling_forever:
    # grid[tuple(p_spawn)] = 2
    stopped = False
    p = deepcopy(p_spawn)
    while not stopped:
        if p[0]+1 >= p_max[0]:
            falling_forever = True
            break
        elif grid[tuple(p + np.array([1,0]))] == 0:
            p[0] += 1 # height, technically
        elif grid[tuple(p + np.array([1,-1]))] == 0:
            p += np.array([1,-1])
        elif grid[tuple(p + np.array([1,1]))] == 0:
            p += np.array([1,1])
        else:
            grid[tuple(p)] = 2
            stopped = True
            break

print(grid)
print(np.sum(grid == 2))

# set bottom layer
for i in range(grid.shape[1]):
    grid[-1,i] = 1
print(grid)
source_covered = False
while not source_covered:
    # grid[tuple(p_spawn)] = 2
    stopped = False
    p = deepcopy(p_spawn)
    while not stopped:
        if grid[tuple(p + np.array([1,0]))] == 0:
            p[0] += 1 # height, technically
        elif grid[tuple(p + np.array([1,-1]))] == 0:
            p += np.array([1,-1])
        elif grid[tuple(p + np.array([1,1]))] == 0:
            p += np.array([1,1])
        elif np.all(p == p_spawn):
            source_covered = True
            grid[tuple(p)] = 2
            break
        else:
            grid[tuple(p)] = 2
            stopped = True
            break

print(grid)
print(np.sum(grid == 2))
