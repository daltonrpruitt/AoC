#01
import numpy as np


inputs = open("input.txt", 'r').read().splitlines()

elves = []
elf = []
for l in inputs :
    if l == "":
        elves.append(elf)
        elf = []
        continue
    elf.append(int(l))
    
totals = []
print(elves[:5])
for e in elves: 
    val = 0
    for c in e:
        val += c
    totals.append(val)

print(totals[:5])
totals.sort(reverse=True)
print(totals[:3])
print("Top 1: ", totals[0])

print("Top three sum: ", sum(totals[:3]))
