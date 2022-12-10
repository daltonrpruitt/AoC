# day 9 : Over 40m for part 1, 20m for part 2

import numpy as np
from copy import deepcopy


# sample = False
sample = False
debug = False

dir_to_coord = {
    "U" : np.array([0,1]),
    "D" : np.array([0,-1]),
    "R" : np.array([1,0]),
    "L" : np.array([-1,0])
}


if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input2.txt", 'r').read().splitlines()

tail_visits = {0:set(), 8:set()}


start_pos = np.array([0,0])
h_pos = deepcopy(start_pos)
tails_pos = [deepcopy(h_pos) for i in range(9)]
tail_visits[0].add((tails_pos[0][0], tails_pos[0][1]))
tail_visits[8].add((tails_pos[8][0], tails_pos[8][1]))

def new_pos(target_pos, mover_pos):
    new_pos = deepcopy(mover_pos)
    delta = target_pos - mover_pos
    abs_ = np.abs(delta)

    if abs_[0] >= 2 and abs_[1] < 1:
        new_pos += np.array([delta[0]//abs_[0],0])
    elif abs_[1] >= 2 and abs_[0] < 1:
        new_pos += np.array([0,delta[1]//abs_[1]])
    elif (abs_[0] > 1 and abs_[1] >= 1) or (abs_[0] >= 1 and abs_[1] > 1):
        new_pos += np.array([delta[0]//abs_[0],delta[1]//abs_[1]])
    return new_pos

for l in lines:
    dir_, num_ = l.split(" ")
    add_dir = dir_to_coord[dir_]
    if not debug: print(l)
    for i in range(int(num_)):
        
        h_pos += add_dir
        tails_pos[0] = new_pos(h_pos, tails_pos[0])
        tail_visits[0].add((tails_pos[0][0], tails_pos[0][1]))

        for t in range(1, len(tails_pos)):
            tails_pos[t] = new_pos(tails_pos[t-1], tails_pos[t])
        tail_visits[8].add((tails_pos[8][0], tails_pos[8][1]))

        if debug:
            print("After",l,":", h_pos, end=" ")
            for t in tails_pos:
                print(t, end=" ")
            print("\n","-"*30)

print("Part 1:", len(tail_visits[0]))
print("Part 2:", len(tail_visits[8]))
