# day 5 : 37:15 for me, for both
from copy import deepcopy
inputs = open("input.txt", 'r').read().splitlines()

def proc_stack_line(line):
    stacks = []
    curr_stack = 0
    for i in range(len(line)//4 + 1):
        if line[i*4] == "[":
            stacks.append(line[i*4+1])
            curr_stack += 1
        elif line[i*4] == " ":
            stacks.append("")
            curr_stack += 1
    return stacks

def get_stacks(lines):
    stack_layers = []
    for l in lines[::-1]:
        stack_layers.append(proc_stack_line(l))
    stacks = [[] for i in range(9)]
    for layer in stack_layers:
        for s in range(len(layer)):
            if layer[s] != "":
                stacks[s].append(layer[s])
    return stacks

lines = []
for l in inputs:
    if(l.find(" 1") >= 0):
        # separate
        break
    lines.append(l)
stacks = get_stacks(lines)
print(stacks)

start = 0
for l in inputs:
    start += 1
    if l == "":
        break

instructions = []
for l in inputs[start:]:
    num_ = int(l[len("move "):l.find("from")])
    from_ = int(l[l.find("from ")+len("from "):l.find(" to ")]) - 1
    to_ = int(l[l.find(" to ")+len(" to "):]) - 1
    instructions.append((num_, from_, to_))

new_stacks = deepcopy(stacks)
for ins in instructions:
    for i in range(ins[0]):
        new_stacks[ins[2]].append(new_stacks[ins[1]].pop())

print(new_stacks)
message = ""
for i in new_stacks:
    message += i[-1]

print(message)

for ins in instructions:
    crates = stacks[ins[1]][-ins[0]:]
    for i in range(ins[0]):
        stacks[ins[1]].pop()
    for c in crates:
        stacks[ins[2]].append(c)

print(stacks)
message = ""
for i in stacks:
    message += i[-1]

print(message)


