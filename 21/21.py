# 21
import time
import numpy as np

debug = True
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()

place = [4,8] if sample else [4,9]


scores = [0,0]
p = 0
roll = 0
count = 0
while all([s < 1000 for s in scores]):
    cur_move = 0
    for i in range(3):
        roll += 1
        cur_move += roll
        count += 1
    place[p] = (place[p] + cur_move - 1) % 10 + 1 
    scores[p] += place[p]
    p = 1 - p

winner = [s >= 1000 for s in scores].index(True)
loser = 1-winner

final_score = scores[loser] * count

print(f"Part 1: Score = {final_score} Time = {time.time()-startTime}s")


rf = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]

def wins(p1,t1,p2,t2):
    if t2 <= 0: return (0,1) # p2 has won (never p1 since p1 about to move)

    w1,w2 = 0,0
    for (r,f) in rf:
        c2,c1 = wins(p2,t2,(p1+r)%10,t1 - 1 - (p1+r)%10) # p2 about to move
        w1,w2 = w1 + f * c1, w2 + f * c2

    return w1,w2

print("Bigger winner universes:",max(wins(3,21,8,21))) 



