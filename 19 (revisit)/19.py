# 19
# Based on https://pastebin.com/ER95t26x
# from https://www.reddit.com/r/adventofcode/comments/rjpf7f/comment/hp9xy8r/?utm_source=share&utm_medium=web2x&context=3
import time
import numpy as np
from itertools import permutations, product
from collections import defaultdict

debug = True
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()


# Loading
if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

# print(lines[:10])

class Point():
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)
    def manhattan_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

class Scanner():
    def __init__(self, detected_points=[], location=None):
        self.detected_points = detected_points
        self.location = location


all_positions = []
cur_positions = []

for line in lines:
    if line.startswith("---"):
        cur_positions = []
    elif line == "":
        all_positions.append(cur_positions.copy())
        cur_positions = None
    else:
        cur_positions.append([int(i) for i in line.split(",")])

if False:
    [print(i[:3]) for i in all_positions[:5]]
    print("Size:",len(all_positions), "by", len(all_positions[0]))

# scanners = [np.array(s) for s in all_positions]
# def gen_rotation_matrices():
#     #  degrees 0  90  180  270
#     cos_vals = 1,  0,  -1,   0
#     sin_vals = 0,  1,  0,   -1

#     mats = []
#     for i in range(3):
#         for i in range(4):
#             pass

# def overlap(s1, s2):
#     pass

# def get_differences: 

# for scanner1 in scanners:
#     for scanner2 in scanners:
#         pass

def rotated_versions(points):
    all_rotated_points = []
    for rot_axes in permutations(['x','y','z']):
        # signs = product([1,-1], repeat=3)
        # print(rot_axes)
        for sign in product([1,-1], repeat=3):
            rot_points = []
            for p in points:
                axes = {'x': p.x, 'y': p.y, 'z': p.z}
                rot_points.append(Point(axes[rot_axes[0]]*sign[0],axes[rot_axes[1]]*sign[1],axes[rot_axes[2]]*sign[2]))
            all_rotated_points.append(rot_points)
    return all_rotated_points

def check_same_shape(located_scanner, unlocated_scanner):
    for rotation in rotated_versions(unlocated_scanner.detected_points):
        counts = defaultdict(int)
 
        for point_1 in rotation:
            for point_2 in located_scanner.detected_points:
                counts[point_2 - point_1] += 1
 
        for k in counts:
            if counts[k] == 12:
                return True, Point(k[0], k[1], k[2]), rotation
 
    return False, None, None

def convert_to_absolute(scanner_location, points):
    new = []
    for point in points:
        new.append(Point(point.x + scanner_location.x, point.y +
                   scanner_location.y, point.z + scanner_location.z))
    return new


def locate_scanners(scanners):
    n = len(scanners)
    located_scanners = {
        0: Scanner(scanners[0].detected_points, Point(0, 0, 0))
    }
 
    while len(located_scanners) != n:
        for i in range(n):
            if i in located_scanners: continue
            unlocated_scanner = scanners[i]
            for j in located_scanners:
                located_scanner = located_scanners[j]
                valid, scanner_location, rotation = check_same_shape(
                    located_scanner, unlocated_scanner)
                if not valid: continue
                newly_located_scanner = Scanner(
                    convert_to_absolute(
                        scanner_location, rotation
                    ),
                    scanner_location
                )
                located_scanners[i] = newly_located_scanner
                break
 
    res = [None] * n
    for i in located_scanners:
        res[i] = located_scanners[i]
    return res

def part1_2(scanners_points):
    scanners = []
    for points in scanners_points:
        scanners.append(Scanner([Point(x,y,z) for x,y,z in points]))
    located_scanners = locate_scanners(scanners)
 
    points = set()
 
    for scanner in located_scanners:
        points.update(scanner.detected_points)
 
    print("Part 1 =", len(points))


    max_found = float('-inf')
    for i in range(len(located_scanners)):
        for j in range(i+1, len(located_scanners)):
            scanner_1 = located_scanners[i]
            scanner_2 = located_scanners[j]
 
            max_found = max_found(res, scanner_1.location.manhattan_dist(
                scanner_2.location))

    print("Part 2 =", max_found)

part1_2(all_positions)
