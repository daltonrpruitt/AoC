# 10
import time

debug = False
startTime = time.time()

lines = open("input.txt", 'r').read().splitlines()


lefts = "([{<"
rights = ")]}>"
points = [3, 57, 1197, 25137]

total_score = 0
# use a stack? (well just a list, but only using .append() and .pop())

symbol_stacks = [] 
# basically, accumulate lefts, pop as find corresponding rights, 
#   fail when right does not match the left on top of stack
for line in lines:
    curr_stack = []
    valid = True
    for sym in line:
        if sym in lefts:
            curr_stack.append(sym)
        elif sym in rights:
            expected_right_idx = lefts.index(curr_stack[-1])
            expected_right = rights[expected_right_idx]
            if sym != expected_right:
                valid = False
                total_score += points[rights.index(sym)]
                if debug: print(f"symbol={sym}, total_score={total_score}")
                break
            else:  # sym == expected_right
                curr_stack.pop()
        else:
            raise ValueError(f"Symbol {sym} is not valid!")
    if valid: symbol_stacks.append(curr_stack)

print(f"Part 1: Score sum={total_score} time={time.time()-startTime}s")
# 369105

added_rights_idxs = []

for curr_stack in symbol_stacks:
    curr_added_rights_idxs = []
    while len(curr_stack) > 0:
        sym = curr_stack.pop()
        curr_added_rights_idxs.append(lefts.index(sym))
    added_rights_idxs.append(curr_added_rights_idxs)

scores = []
for right_idxs in added_rights_idxs:
    score = 0
    for idx in right_idxs:
        score *= 5
        score += idx+1
    scores.append(score)
scores.sort()
print(len(scores))
median = scores[(len(scores)-1)//2]

print(f"Part 2: Score median={median } time={time.time()-startTime}s")
# 3999363569

print("Done")