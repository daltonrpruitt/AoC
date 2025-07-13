# day 16
# had to get help initially. was quite out of it...

import numpy as np
from copy import deepcopy


sample = True
# sample = False
debug =  True


if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

gusts = lines[0]
grid = np.zeros((3*2022,7), np.int16)

r = 0
room_width = 7

rocks = [
    np.array([[1,1,1,1]], np.int16),
    np.array([[0,1,0],
              [1,1,1],
              [0,1,0]], np.int16),
    np.array([[1,1,1],
              [0,0,1],
              [0,0,1]], np.int16),
    np.array([[1],[1],[1],[1]], np.int16),
    np.array([[1,1],
              [1,1]], np.int16),
]

def current_height(room, hint=0):
    curr = int(hint)
    while True:
        # if debug: print(room[curr])
        detected = False
        for i in range(room.shape[1]):
            # if debug: print(room[curr, i])            
            if room[curr, i] == 1:
                curr += 1
                detected = True
                break
        if not detected:
            break
    return curr

def check_overlap(room, rock, new_pos):
    h, w = rock.shape
    for i in range(h):
        for j in range(w):
            if rock[i,j] == 1 and room[tuple(new_pos+np.array([i,j]))] == 1: 
                return True
    return False

def can_move_horizontal(room, rock, pos, horizontal_move):
    h, w = rock.shape
    if pos[1] + horizontal_move + w >= room_width or pos[1] + horizontal_move < 0: 
        return False
    if check_overlap(room, rock, pos + np.array([0, horizontal_move], np.int8)):
        return False
    return True


def can_move_down(room, rock, curr_pos):
    h, w = rock.shape
    if curr_pos[0] == 0: 
        return False
    new_pos = curr_pos + np.array([-1, 0], np.int16)
    # if np.all(rock.shape == rocks[2].shape) and np.all(rock == rocks[2]):
    #     print("Checking if can put rock here")
    #     for i in range(7):
    #         print(room[curr_pos[0] - i])
    if check_overlap(room, rock, new_pos):
        return False
    return True

def move_rock(room, moves, rock):
    pass

starting_offset = np.array([3,2], np.int16)
height = int(0)
gust_idx = 0
def add_rock(room, rock):
    global height
    global gust_idx
    pos = starting_offset + np.array([height,0], np.int16)
    # next_move = np.array([-1,0], np.int16)
    while True:
        
        # move horizontal
        horizontal_move = -1 if gusts[gust_idx % len(gusts)] == "<" else 1 
        print(horizontal_move)
        gust_idx += 1
        if can_move_horizontal(room, rock, pos, horizontal_move):
            # if debug: print("Move horizontal by", horizontal_move)
            pos += np.array([0,horizontal_move], np.int16)
        
        # move down
        if can_move_down(room, rock, pos):
            # if debug: print("moving down")
            pos += np.array([-1,0], np.int16)
            continue
        else:
            h, w = rock.shape
            for i in range(h):
                for j in range(w):
                    old_val = room[tuple(pos+np.array([i,j]))]
                    rock_val = rock[i,j]
                    new_val = 0
                    if old_val == 1 or rock_val == 1:
                        new_val = 1
                    room[tuple(pos+np.array([i,j]))] = new_val
            height = current_height(room, int(pos[0]))
            return 
            # if height >= 2022:
            #     return True
            # else: 
            #     return False

    # while True:
        # 
def print_room(room, size = 10, start=0):
    for i in range(size):
        x = size-i-1 + start
        if x < 0: break
        print(x, ":", room[x])
    print()

for i in range(2022):
    # if 
    add_rock(grid, rocks[i%5])
    if debug: 
        print_room(grid, 10, height-7)
    if i % 100 == 0: 
        print("Added rock",i)
        # break

print("Num rocks =", i+1)
print_room(grid, 10, height-7)
print("Part 1:", height, current_height(grid, hint=height-7))
np.savetxt("output.txt", grid[:height+3], fmt='%.1d')