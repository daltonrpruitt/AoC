import numpy as np
from utils.inputs import *

inputs = open("input.txt", 'r').read().splitlines()
rounds = [i.split(" ") for i in inputs]

print(rounds[:10])

them = {"A": 0, 
    "B": 1,
    "C": 2}
you = {"X": 0,
    "Y": 1,
    "Z": 2}

total = 0
for rnd in rounds:
    l = them[rnd[0]]
    r = you[rnd[1]]
    total += r+1
    if l == r:
        total += 3
    elif (l+1) % 3 == r:
        total += 6
    elif (l-1) % 3 == r:
        pass
    else: 
        raise Exception("Should not get here!")
print(total)
        