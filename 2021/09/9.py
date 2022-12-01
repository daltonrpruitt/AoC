# 09
import time
import numpy as np


startTime = time.time()

lines = open("input.txt", 'r').read().splitlines()
lines =  [' '.join([c for c in l]) for l in lines]
# print(lines[:3])

arrs = [np.fromstring(l,dtype=int,sep=" ",) for l in lines]
# print(arrs[:10])
heightmap = np.stack(arrs, axis=0)
# print(heightmap[:10,:10])


is_min = np.ones(shape=heightmap.shape, dtype=int)

size = heightmap.shape[0]
for i in range(size):
    if i == 0:      is_min[i,:] = is_min[i,:] == 1
    else:           is_min[i,:] = np.logical_and(heightmap[i-1,:] > heightmap[i,:], is_min[i,:])

    if i==size-1:   is_min[i,:] = is_min[i,:] == 1
    else:           is_min[i,:] = np.logical_and(heightmap[i+1,:] > heightmap[i,:], is_min[i,:])
        
for j in range(size):
    if j == 0:      is_min[:,j] = is_min[:,j] == 1
    else:           is_min[:,j] = np.logical_and(heightmap[:,j-1] > heightmap[:,j], is_min[:,j])

    if j==size-1:   is_min[:,j] = is_min[:,j] == 1
    else:           is_min[:,j] = np.logical_and(heightmap[:,j+1] > heightmap[:,j], is_min[:,j])

scores = np.multiply(is_min, heightmap) + is_min

window = 10
offset = 25
# print(is_min[:10])
print(heightmap.shape, is_min.shape, scores.shape)
print(heightmap[offset:offset+window,offset:offset+window])
print(is_min[offset:offset+window,offset:offset+window])
print(scores[offset:offset+window,offset:offset+window])

sum = scores.sum().sum()
print(f"Part 1: Score sum={sum} time={time.time()-startTime}s")



basins = -1 * np.ones(heightmap.shape, dtype=int)
for i in range(size):
    for j in range(size):
        if is_min[i,j]:
            basins[i,j] = is_min[i,j] * (i*size + j)
print(basins[offset:offset+window,offset:offset+window])

for d in range(10):
    for i in range(size):
        if i != 0:
            basins[i-1, :] += np.multiply(np.logical_and.reduce((
                basins[i, :] > -1,
                basins[i-1, :] == -1,
                heightmap[i-1, :] >= heightmap[i, :],
                heightmap[i-1, :] < 9
            )), basins[i, :]+1)

        if i != size-1:
            basins[i+1, :] += np.multiply(np.logical_and.reduce((
                basins[i, :] > -1,
                basins[i+1, :] == -1,
                heightmap[i+1, :] >= heightmap[i, :],
                heightmap[i+1, :] < 9
            )), basins[i, :]+1)


    
    for j in range(size):
        if j != 0:
            basins[:, j-1] += np.multiply(np.logical_and.reduce((
                basins[:, j] > -1,
                basins[:, j-1] == -1,
                heightmap[:, j-1] >= heightmap[:, j],
                heightmap[:, j-1] < 9
            )), basins[:, j]+1)

        if j != size-1:
            basins[:, j+1] += np.multiply(np.logical_and.reduce((
                basins[:, j] > -1,
                basins[:, j+1] == -1,
                heightmap[:, j+1] >= heightmap[:, j],
                heightmap[:, j+1] < 9
            )), basins[:, j]+1)

print(basins[offset:offset+window,offset:offset+window])

uniq_basins = np.unique(basins, return_counts=True)
# sorted_sizes =  uniq_basins[1]
sorted_sizes = sorted(uniq_basins[1], reverse=True)
print(sorted_sizes)
total = sorted_sizes[1] * sorted_sizes[2] * sorted_sizes[3]  # ignore -1, which has most


print(f"Part 2: Total sizes of big 3={total} time={time.time()-startTime}s")

# np.savetxt("basins.txt", basins, fmt="%d")
print("Done")