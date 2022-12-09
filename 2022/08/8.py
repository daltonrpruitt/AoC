# day 8 : Over 40m for part 1, 20m for part 2

import numpy as np
from copy import deepcopy


sample = False

if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

width = len(lines[0])
length = len(lines)


grid = np.array([list(map(int, i)) for i in lines], np.int8) + 1

# print(grid)
size = grid.shape[0]


left_visible = np.ones(shape=(size,size),dtype=int)

for i in range(1,size):
    shifted_i_plus = np.concatenate((
        np.zeros(shape=(size,i),dtype=int),
        grid[:,:size-i]
        ), axis=1)
    left_visible = np.logical_and(left_visible, grid > shifted_i_plus)
# print(left_visible)

right_visible = np.ones(shape=(size,size),dtype=int)

for i in range(1,size):
    shifted_i_minus = np.concatenate((
        grid[:,i:],
        np.zeros(shape=(size,i),dtype=int)
        ), axis=1)
    right_visible = np.logical_and(right_visible, grid > shifted_i_minus)
# print(right_visible)

up_visible = np.ones(shape=(size,size),dtype=int)

for i in range(1,size):
    shifted_j_plus = np.concatenate((
        np.zeros(shape=(i,size),dtype=int),
        grid[:size-i,:]
        ), axis=0)
    up_visible = np.logical_and(up_visible, grid > shifted_j_plus)
# print(up_visible)

down_visible = np.ones(shape=(size,size),dtype=int)

for i in range(1,size):
    shifted_j_minus = np.concatenate((
        grid[i:,:],
        np.zeros(shape=(i,size),dtype=int),
        ), axis=0)
    down_visible = np.logical_and(down_visible, grid > shifted_j_minus)
# print(down_visible)

total_visible = np.zeros(shape=(size,size),dtype=int)
for a in (left_visible, right_visible, up_visible, down_visible):
    total_visible = np.logical_or(total_visible, a)
total = np.sum(total_visible)
print("Part 1: ",total)

########################################################
########################################################
########################################################
########################################################

print(grid)

left_count = np.zeros(shape=(size,size),dtype=int)
left_visible = np.ones(shape=(size,size),dtype=int)
for i in range(1,size):
    shifted_i_plus = np.concatenate((
        np.zeros(shape=(size,i),dtype=int),
        grid[:,:size-i]
        ), axis=1)
    left_count += np.logical_and(shifted_i_plus>0, left_visible)
    left_visible = np.logical_and(shifted_i_plus>0, np.logical_and(left_visible, grid > shifted_i_plus))
    # left_count += left_visible
    # print(left_visible)
    # print(left_count)
print(left_count)


right_count = np.zeros(shape=(size,size),dtype=int)
right_visible = np.ones(shape=(size,size),dtype=int)
for i in range(1,size):
    shifted_i_minus = np.concatenate((
        grid[:,i:],
        np.zeros(shape=(size,i),dtype=int)
        ), axis=1)
    right_count += np.logical_and(shifted_i_minus>0, right_visible)
    right_visible = np.logical_and(shifted_i_minus>0, np.logical_and(right_visible, grid > shifted_i_minus))
print(right_count)


up_count = np.zeros(shape=(size,size),dtype=int)
up_visible = np.ones(shape=(size,size),dtype=int)
for i in range(1,size):
    shifted_j_plus = np.concatenate((
        np.zeros(shape=(i, size),dtype=int),
        grid[:size-i,:]
        ), axis=0)
    up_count += np.logical_and(shifted_j_plus>0, up_visible)
    up_visible = np.logical_and(shifted_j_plus>0, np.logical_and(up_visible, grid > shifted_j_plus))

print(up_count)


down_count = np.zeros(shape=(size,size),dtype=int)
down_visible = np.ones(shape=(size,size),dtype=int)
for i in range(1,size):
    shifted_j_minus = np.concatenate((
        grid[i:,:],
        np.zeros(shape=(i, size),dtype=int)
        ), axis=0)
    down_count += np.logical_and(shifted_j_minus>0, down_visible)
    down_visible = np.logical_and(shifted_j_minus>0, np.logical_and(down_visible, grid > shifted_j_minus))
print(down_count)


prods = left_count * right_count * up_count * down_count
print(prods)
ans = np.max(prods)
print("Part 2: ",ans)

import matplotlib.pyplot as plt


plt.imshow(prods, cmap='hot', interpolation='nearest')
plt.savefig("scenic_scores.png")

plt.imshow(left_count, cmap='hot', interpolation='nearest')
plt.savefig("left_count.png")


plt.imshow(right_count, cmap='hot', interpolation='nearest')
plt.savefig("right_count.png")

plt.imshow(up_count, cmap='hot', interpolation='nearest')
plt.savefig("up_count.png")
plt.imshow(down_count, cmap='hot', interpolation='nearest')
plt.savefig("down_count.png")
