# 04
import time
import numpy as np


startTime = time.time()

positions = np.array(open("input.txt", 'r').read().split(','),dtype=int)

winning_val_usage = [-1,np.inf]
for val in range(len(positions)):
    usage = np.abs(np.subtract(positions,val)).sum()
    if usage < winning_val_usage[1]:
        winning_val_usage = [val, usage]
print(f"Part 1: pos={winning_val_usage[0]},usage={winning_val_usage[1]} time={time.time()-startTime}s")


startTime = time.time()

winning_val_usage = [-1,np.inf]
usages = []
for val in range(len(positions)):
    abs_differences = np.abs(np.subtract(positions,val))
    n_plus_1 = np.add(abs_differences, 1)
    n_n_plus1 = np.multiply(abs_differences, n_plus_1)
    usage = int(np.divide(n_n_plus1, 2).sum())
    # print(abs_differences[:10])
    # print(n_plus_1[:10])
    # print(n_n_plus1[:10])
    # print(usage[:10])
    # exit()
    # usage = np.divide(np.multiply(abs_differences, np.add(abs_differences, 1)),2).sum()
    # usage = int(usage)
    usages.append(usage)
    if usage < winning_val_usage[1]:
        winning_val_usage = [val, usage]
print(f"Part 2: pos={winning_val_usage[0]},usage={winning_val_usage[1]} time={time.time()-startTime}s")
# 337, 58701598761 too high...
# 473, 93009400 too high...

with open("usages.txt","w") as f:
    for i in range(len(positions)):
        f.write(f"{i},{usages[i]}\n")

print("Done")