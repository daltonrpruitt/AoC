# 11
import time
import numpy as np

debug = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()

# Loading
lines = open("input.txt", 'r').read().splitlines()
lines = [" ".join([c for c in l]) for l in lines]
lines = [np.fromstring(l,dtype=int,sep=" ") for l in lines] 
energies = np.stack(lines, axis=0)

# keeping track
flashes_count = np.zeros(shape=energies.shape, dtype=int)
size = energies.shape[0]
# Stepping:
for i in range(10000):
    debug_log("Round"+str(i))
    flashed_this_round = np.zeros(shape=energies.shape, dtype=int)
    energies += 1
    ready_to_flash = energies > 9
    while ready_to_flash.sum().sum() > 0:
        debug_log(ready_to_flash)
        flashes_count += ready_to_flash
        flashed_this_round += ready_to_flash
        debug_log(energies)
       
        # print(np.roll(ready_to_flash, shift=1, axis=1))
        # print(np.roll(ready_to_flash, shift=1, axis=1)[:,:size-1])
        # print(np.zeros(shape=(size,1)))
        shifted_i_plus = np.concatenate((
            ready_to_flash[:,1:],
            np.zeros(shape=(size,1),dtype=int)
            ), axis=1)
        shifted_i_minus = np.concatenate((
            np.zeros(shape=(size,1),dtype=int),
            ready_to_flash[:,:size-1]
            ), axis=1)
        shifted_j_plus = np.concatenate((
            ready_to_flash[1:,:],
            np.zeros(shape=(1,size),dtype=int)
            ), axis=0)
        shifted_j_minus = np.concatenate((
            np.zeros(shape=(1,size),dtype=int),
            ready_to_flash[:size-1,:]
            ), axis=0)
        o, w = 5, 5
        # debug_log(ready_to_flash[o:o+w,o:o+w])
        # print(shifted_i_plus[o:o+w,o:o+w], shifted_i_minus[o:o+w,o:o+w], shifted_j_plus[o:o+w,o:o+w], shifted_j_minus[o:o+w,o:o+w], sep="\n")
        i_p_j_p = np.concatenate((
            shifted_i_plus[1:,:],
            np.zeros(shape=(1,size),dtype=int)
            ), axis=0)
        i_p_j_m = np.concatenate((
            np.zeros(shape=(1,size),dtype=int),
            shifted_i_plus[:size-1,:]
            ), axis=0)
        i_m_j_p = np.concatenate((
            shifted_i_minus[1:,:],
            np.zeros(shape=(1,size),dtype=int)
            ), axis=0)
        i_m_j_m = np.concatenate((
            np.zeros(shape=(1,size),dtype=int),
            shifted_i_minus[:size-1,:]
            ), axis=0)

        energies += shifted_i_plus + shifted_i_minus + shifted_j_plus + shifted_j_minus + i_p_j_p + i_p_j_m + i_m_j_p + i_m_j_m
        # print(energies)

        # for i in range(size):
        #     if i != 0: energies[i,:] = energies[i,:] +ready_to_flash[i-1,:]
        #     if i != size-1: energies[i,:] = energies[i,:] + ready_to_flash[i+1,:]
        # for j in range(size):
        #     if j != 0: energies[:,j] = energies[:,j] +ready_to_flash[:,j-1]
        #     if j != size-1: energies[:,j] = energies[:, j] + ready_to_flash[:,j+1]
        debug_log(energies)
        energies = energies * (1-flashed_this_round)
        ready_to_flash = np.logical_and(energies > 9, np.logical_and(flashed_this_round == 0, ready_to_flash != 1))
    # after flashing stops
    energies = energies * (1-flashed_this_round) # set to 0
    if i == 99:
        print(flashes_count)
        print(f"Part 1: Total Flashes={flashes_count.sum().sum()} time={time.time()-startTime}s")
        # 1625

    # print(energies)

    if flashed_this_round.sum().sum() == size**2:
        print(f"All flashed in step {i+1}!")
        print(energies)
        print(flashed_this_round)
        print(f"Total flashes = {flashes_count.sum().sum()}")
        break

print("Done")