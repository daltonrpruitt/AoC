# day 6 : 17.24 for me, for both

inputs = open("input.txt", 'r').read().splitlines()[0]
counts = dict()

for i in range(3):
    if inputs[i] not in counts:
        counts[inputs[i]] = 0
    counts[inputs[i]] += 1
for i in range(3,len(inputs)-3):
    if inputs[i] not in counts:
        counts[inputs[i]] = 0
    counts[inputs[i]] += 1
    passed = True
    for c in counts:
        if counts[c] > 1:
            passed = False
            break
    counts[inputs[i-3]] -= 1
    if counts[inputs[i-3]] == 0:
        del counts[inputs[i-3]]
    if passed:
        print("Number read:", i+1)
        print("Message: ", inputs[i-3:i+1])
        break
    
counts = dict()

for i in range(13):
    if inputs[i] not in counts:
        counts[inputs[i]] = 0
    counts[inputs[i]] += 1
for i in range(13,len(inputs)-13):
    if inputs[i] not in counts:
        counts[inputs[i]] = 0
    counts[inputs[i]] += 1
    passed = True
    for c in counts:
        if counts[c] > 1:
            passed = False
            break
    counts[inputs[i-13]] -= 1
    if counts[inputs[i-13]] == 0:
        del counts[inputs[i-13]]
    if passed:
        print("Number read:", i+1)
        print("Message: ", inputs[i-13:i+1])
        break
