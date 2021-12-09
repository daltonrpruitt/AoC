#01

lines = open("input.txt", 'r').readlines()
vals = [int(l) for l in lines]

inc = 0
last = vals[0]
for i in range(1,len(vals)):
    cur = vals[i]
    if cur > last:
        inc += 1
    last = cur

print("Num times increment:",inc)

#last_sum = sum(vals[i] for i in range(3)])
inc = 0
last = vals[0]
for i in range(3,len(vals)):
    cur = vals[i]
    if cur > last:
        inc += 1
    last = vals[i-3+1]

print("Num times increment (window):",inc)
