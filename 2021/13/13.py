# 13
import time
import numpy as np

debug = False
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()


# Loading
if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()
dots = []
folds = []

i = 0
start_folds = False

for line in lines:
    if debug: print(line)
    if not start_folds:
        if line == '':
            if debug: print("End of points")
            start_folds = True
            continue
        xstr, ystr = line.split(",")
        dots.append(tuple([int(xstr),int(ystr)]))
    else:
        axis, value = line.split("=")
        axis = axis[-1] # x or y only
        folds.append([axis, int(value)])


# folds = []
# for l in range(i, len(lines)):

points = set(dots)
def fold(points, folds):
    # just 1st fold
    output_points = points.copy()
    for fold in folds:
        # points = points
        new_points_set = output_points.copy()
        for pt in output_points:
            # new_pt = ())
            if fold[0] == "x":
                if pt[0] > fold[1]:
                    new_point = (fold[1]-abs(pt[0] - fold[1]),pt[1]) 
                else:
                    new_point = pt 
            else:
                if pt[1] > fold[1]:
                    new_point = (pt[0],fold[1]-abs(pt[1] - fold[1]))
                else:
                    new_point = pt 

            new_points_set.remove(pt)
            new_points_set.add(new_point)
        output_points = new_points_set

        if debug:
            print(f"After {len(folds)} folds, points left = {len(output_points)}  Time={time.time() - startTime}s")
    if not debug: 
        print(f"After {len(folds)} folds, points left = {len(output_points)}  Time={time.time() - startTime}s")
    return output_points

def part2(points, folds):
    pass

fold(points, [folds[0]])
# 847

render_points = fold(points, folds)

# 185
print(len(render_points))
for j in range(14):
    for i in range(45):
        # print(i,",",j)
        if (i, j) in render_points:
            print("#",end="")
        else: 
            print("_",end="")
    print(" ")
print("Done")