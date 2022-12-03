import numpy as np
from utils.inputs import *

inputs = open("input.txt", 'r').read().splitlines()
rounds = [i.split(" ") for i in inputs]

print(rounds[:10])

them = {"A": 0, 
    "B": 1,
    "C": 2}
outcome = {"X": 0,
    "Y": 1,
    "Z": 2}

total = 0
for rnd in rounds:
    l = them[rnd[0]]
    o = outcome[rnd[1]]
    total += o*3 +1
    if o == 0:
        total += (l-1) % 3
    elif o == 1:
        total += l
    elif o == 2:
        total += (l+1) % 3

print(total)
        