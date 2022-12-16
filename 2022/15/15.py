# day 14

import numpy as np
from copy import deepcopy

# sample = True
sample = False

if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

s_b = []
for l in lines:
    s, b = l.split(": closest beacon is at ")
    s = s[len("Sensor at "):]
    
    s = s.split(",")
    s[0] = int(s[0][s[0].find("x=") + len("x="):])
    s[1] = int(s[1][s[1].find("y=")+len("y="):])
    b = b.split(",")
    b[0] = int(b[0][b[0].find("x=") + len("x="):])
    b[1] = int(b[1][b[1].find("y=")+len("y="):])
    
    s_b.append(np.array([s,b],dtype=np.int32))

y = 2_000_000
if sample: y = 10

cleared_ranges = []

def merge_ranges(ranges, range):
    found_relevant_range = False
    x_min, x_max = range
    for c in ranges:
        if x_min < c[0] and x_max >= c[0]:
            c[0] = x_min
            found_relevant_range = True
        if x_min <= c[1] and x_max > c[1]:
            c[1] = x_max
            found_relevant_range = True
        if found_relevant_range:
            break
        if x_min >= c[0] and x_max <= c[1]:
            found_relevant_range = True
            break
    return found_relevant_range

for s, b in s_b:
    # dist = max(abs(b[0] - s[0]), abs(b[1] - s[1]))
    # print(b - s)
    dist = np.sum(np.abs(b-s))
    # print(dist)
    spread = abs(s[1]-y)
    if spread > dist:
        continue
    x_min, x_max = s[0]-(dist-spread), s[0]+(dist-spread)

    if not merge_ranges(cleared_ranges, [x_min, x_max]):
        cleared_ranges.append([x_min, x_max])

def comp(r1, r2):
    if r1[0] < r2[0]:
        return 1
    elif r1[0] > r2[1]:
        return -1
    else:
        return 0
    
from functools import cmp_to_key
cleared_ranges.sort(key=cmp_to_key(comp), reverse=True)
print(cleared_ranges)
merged_ranges = []
for c in cleared_ranges:
    if not merge_ranges(merged_ranges, c):
        merged_ranges.append(c)

print(merged_ranges)

total = 0
for r in merged_ranges:
    total += r[1] - r[0]
    
print("Part 1:", total)

mx = 4_000_000
def too_wide(ranges):
    if len(ranges) != 1:
        return False
    if ranges[0][0] <= 0 and ranges[0][1] >= mx:
        return True
    return False

# range_lists = [[] for i in range(4_000_000)]
likely_x = None
likely_y = None

def solve(l, i, e):
    for i in range(i,e):
        ranges = []
        for s, b in s_b:
            # dist = max(abs(b[0] - s[0]), abs(b[1] - s[1]))
            # print(b - s)
            dist = np.sum(np.abs(b-s))
            # print(dist)
            spread = abs(s[1]-i)
            if spread > dist:
                continue
            x_min, x_max = s[0]-(dist-spread), s[0]+(dist-spread)

            if not merge_ranges(ranges, [x_min, x_max]):
                ranges.append([x_min, x_max])
            if too_wide(ranges):
                break
        
        f = 10
        while f > 0:
            merged_ranges = []
            ranges.sort(key=cmp_to_key(comp), reverse=True)
            for c in ranges:
                if not merge_ranges(merged_ranges, c):
                    merged_ranges.append(c)
            ranges = merged_ranges
            if len(ranges) > 2:
                break
            f -= 1
            
        if i % 10_000 == 0:
            print("finished with i =", i)
        
        if too_wide(ranges):
            continue

        if len(ranges) < 2:
            continue
        if len(ranges) == 2:
            ranges.sort(key=cmp_to_key(comp), reverse=True)
            print(i, ranges)
            assert(ranges[1][0] - 1 == ranges[0][1] + 1)
            l.acquire()
            likely_x = np.int(ranges[1][0] - 1)
            likely_y = np.int(i)
            print(likely_x, likely_y)
            print("Part 2:", likely_x * 4000000 + likely_y)
            stop = True
            break

from multiprocessing import Process, Lock
if __name__ == "__main__":
    lck = Lock()
    mn = 1_000_000
    for num in range(10):
        rng = (mx-mn)//10
        i = mn + rng*num
        Process(target=solve, args=(lck, i, i+rng)).start()

    # print(likely_x, likely_y)
    # print("Part 2:", likely_x * 4000000 + likely_y)

# 10852579132904 - too low
# 10852583132904
# 10852583132905 - too high