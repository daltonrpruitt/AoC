# 04
import numpy as np
import copy

file_lines = open("input.txt", 'r').read().splitlines()

# x1, y1 -> x2, y2
line_commands = []
for l in file_lines:
    sides = l.split(' -> ')
    line_commands.append([
        np.fromstring(sides[0], sep=',', dtype=int),
        np.fromstring(sides[1], sep=',', dtype=int)
        ])

debug_lines = False
# if debug_lines:
counter = 0
tallies = np.zeros(shape=(990,990))
for pt1, pt2 in line_commands:
    for ord in (0,1):
        if pt1[ord] == pt2[ord]:
            start, end = pt1[1 - ord],  pt2[1 - ord]
            dir = 1
            if start > end:
                dir =  -1
            if debug_lines:
                print("#"*10+f"\n  Line #{counter}:")
            i = start
            while i != end+dir:
                new_pt = np.array(pt1)
                new_pt[1 - ord] = i
                tallies[new_pt[0]][new_pt[1]] += 1
                i += dir
                ab_len = 2 # abbreviated length
                if debug_lines:
                    print(new_pt)
                    if abs(start - end) > 5 and abs(start - i) > ab_len and abs(end - i) > ab_len:
                        print(" ... ")
                        i = end - dir*ab_len
            if debug_lines:
                print("-"*10)

            
    counter += 1
    if debug_lines and counter > 5:
        break

print(tallies.shape)

crosses = (tallies > 1).sum() 
print("Part 1: crosses =",crosses) # 6548

np.savetxt("tallies.txt", tallies, fmt="%d")
# np.savetxt("crosses.txt", crosses, fmt="%d")


# print("Done")


debug_lines = False
counter = 0
for pt1, pt2 in line_commands:
    already_processed = False
    for ord in (0,1):
        if pt1[ord] == pt2[ord]:
            already_processed = True
            counter+=1
            break
    if already_processed: continue
    slope = 1
    if (pt2[1] - pt1[1])/(pt2[0]-pt1[0]) < 0:
        slope = -1
    if pt2[0]-pt1[0] < 0:
        pt2, pt1 = pt1, pt2
    if debug_lines:
        print("#"*10+f"\n  Line #{counter}:", pt1, "->", pt2)
    for i in range(pt2[0]-pt1[0] + 1):
        new_pt = np.array(pt1)
        new_pt[0] += i
        new_pt[1] += i*slope
        if debug_lines: print(new_pt)
        tallies[new_pt[0]][new_pt[1]] += 1
    counter+=1
crosses = (tallies > 1).sum() 
print(crosses) 
# 19663
# 19635 is too low

np.savetxt("tallies_with_diagonals.txt", tallies, fmt="%d")
