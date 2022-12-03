
sacks = open("input.txt", 'r').read().splitlines()


val_a = 1
val_A = 27

total = 0
for s in sacks:
    # print(s)
    mid = len(s) // 2
    l = s[:mid]
    r = s[mid:]
    # print(l)
    # print(r)
    l = set(l)
    r = set(r)
    # print(l)
    # print(r)
    same = l.intersection(r)
    # print(same)
    assert(len(same) == 1)
    for v in same:
        if(v >= 'a' <= 'z'):
            total += ord(v) - ord("a") + val_a
        elif(v >= 'A' <= 'Z'):
            total += ord(v) - ord("A") + val_A
    
print(total)

total = 0
for idx in range(len(sacks)//3):
    elves = [set(sacks[i]) for i in range(idx*3, idx*3+3)]
    same = elves[0].intersection(elves[1])
    same = same.intersection(elves[2])
    assert(len(same) == 1)
    for v in same:
        if(v >= 'a' <= 'z'):
            total += ord(v) - ord("a") + val_a
        elif(v >= 'A' <= 'Z'):
            total += ord(v) - ord("A") + val_A
    
print(total)
        