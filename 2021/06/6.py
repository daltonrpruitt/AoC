# 04
import time
import numpy as np

def part1():
    startTime = time.time()

    fish_timers = list(map(int, open("input.txt", 'r').read().split(',')))
    for i in range(80):
        start_len = len(fish_timers)
        for fish in range(start_len-1,-1,-1): # work backwards to avoid touching new ones
            if fish_timers[fish] == 0:
                fish_timers.append(8)
                fish_timers[fish] = 6
            else:
                fish_timers[fish] -= 1
        print(f"Day {i}: fish = {len(fish_timers)}")

    print(f"First tally = {len(fish_timers)}, time={time.time()-startTime}s")

def part2():
    startTime = time.time()
    fish_timers =  np.array(list(map(int, open("input.txt", 'r').read().split(','))))
    fishes = np.unique(fish_timers, return_counts=True)
    fishes_tallies = [0 for i in range(9)]
    # print(fishes)
    for i in range(len(fishes[0])):
        # print(i, fishes[0][i], fishes[1][i])
        fishes_tallies[fishes[0][i]] = fishes[1][i]
    # print(fishes_tallies)
    print(fishes_tallies)
    for i in range(256):
        new_fishes_tallies = [0 for j in range(9)]
        for day in range(8): 
            new_fishes_tallies[day] = fishes_tallies[day+1]

        new_fishes_tallies[8] += fishes_tallies[0]
        new_fishes_tallies[6] += fishes_tallies[0]
        fishes_tallies = new_fishes_tallies
        # print(fishes_tallies)
        print(f"Day {i}: fish = {sum(fishes_tallies)}")

    print(f"Second tally = {sum(fishes_tallies)}, time={time.time()-startTime}s")

# part1()
part2()

