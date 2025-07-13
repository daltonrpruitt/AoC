# day 16
# Nah brah. Completely annoyed by this one. Basically copied this beauty: 
# https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py

import re

# sample = True
sample = False

if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

# from https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py
lines = [re.split("[\\s=;,]+",x ) for x in lines]

V = {x[1]: set(x[10:]) for x in lines}
P = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
S = {x: 1<<i for i, x in enumerate(P)}
T = {x: {y: 1 if y in V[x] else float("+inf") for y in V} for x in V}
if sample:
    print("V = ", V)
    print("P = ", P)
    print("S = ", S)
    print("T = ", T)
for i in T:
    for j in T:
        for k in T:
            T[j][k] =  min(T[j][k], T[j][i]+T[i][k])
if sample:
    print("T = ", T)

def visit(v, budget, state, flow, answer):
    answer[state] = max(answer.get(state,0), flow)
    for u in P:
        newbudget = budget - T[v][u] - 1
        if S[u] & state or newbudget <= 0: continue
        visit(u, newbudget, state | S[u], flow + newbudget * P[u], answer)
    return answer

total1 = max(visit('AA', 30, 0, 0, {}).values())

visited2 = visit('AA', 26, 0, 0, {})
total2 = max(v1+v2 for k1, v1 in visited2.items() 
                   for k2, v2 in visited2.items() if not k1 & k2)
if sample: print(visited2.items())
print("Part 1:", total1)
print("Part 2:", total2)


