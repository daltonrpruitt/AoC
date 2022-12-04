# day 4 : 18:06 for me, for both

sacks = open("input.txt", 'r').read().splitlines()
print(sacks[0].split(","))
ranges = [s.split(",") for s in sacks]
for r in ranges:
    spl = r[0].split("-")
    r[0] = set(range(int(spl[0]), int(spl[1])+1))
    spl = r[1].split("-")
    r[1] = set(range(int(spl[0]), int(spl[1])+1))
    

# print(ranges[:10])
num_subsets =0
for r in ranges:
    inter = r[0].intersection(r[1])
    assert(inter == r[1].intersection(r[0]))
    if inter == r[0] or inter == r[1]:
        num_subsets += 1

num_overlaps = 0
for r in ranges:
    inter = r[0].intersection(r[1])
    if len(inter) > 0:
        num_overlaps += 1

print(num_subsets, num_overlaps)
