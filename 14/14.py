# 14
import time
import numpy as np

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

seed = lines[0]
rules = {}

for line in lines[2:]:
    left, right = line.split(" -> ")
    assert(len(left) == 2 )
    assert len(right) == 1
    rules[left] = right 



def score_poly(poly):
    counts = {}
    for char in poly:
        if char in counts.keys():
            counts[char] += 1
        else:
            counts[char] = 1
    count_min, count_max = min(counts.values()), max(counts.values()), 
    return count_max - count_min

def polymerize(in_seed, rules):
    new_poly = ""
    for i in range(len(in_seed)-1):
        pair = in_seed[i]+in_seed[i+1]
        if pair in rules.keys():
            new_poly += pair[0] + rules[pair]
        else:
            new_poly += pair[0]
    return new_poly + in_seed[-1]


def multi_steps(steps):
    local_seed = seed
    for i in range(steps):
        local_seed = polymerize(local_seed, rules)
        if debug:
            print(f"After {i+1} steps, len = {len(local_seed)} Time={time.time() - startTime}s")
    
    print(f"After {i+1} steps, score = {score_poly(local_seed)} Time={time.time() - startTime}s")

def part1():
    multi_steps(10)

def part2():
    counts = {}
    for pair in rules.keys():
        counts[pair] = 0
    for c in range(len(seed)-1):
        counts[seed[c:c+2]] += 1
    
    for i in range(40):
        new_counts = {}
        for pair, val in counts.items():
            if pair in rules.keys():
                left_pair, right_pair = pair[0]+rules[pair],rules[pair]+pair[1] 
                if left_pair not in new_counts.keys():
                     new_counts[left_pair] = 0
                if right_pair not in new_counts.keys(): 
                     new_counts[right_pair] = 0
                new_counts[left_pair] += val
                new_counts[right_pair] += val
            else:
                new_counts[pair] = val
            
        print(f"After {i+1} steps, len = {sum(new_counts.values())+1} Time={time.time() - startTime}s")
        counts = new_counts
    char_counts = {}
    for pair, val in counts.items():
        if pair[0] not in char_counts.keys():
            char_counts[pair[0]] = 0
        char_counts[pair[0]] += val
    char_counts[seed[-1]] += 1

    mi, ma = min(char_counts.values()), max(char_counts.values())
    print(f"After {i+1} steps, score = {ma - mi} Time={time.time() - startTime}s")
    
part1()
# 2375

part2()
# 1106636405205 too low....
# 1976896901756

print("Done")