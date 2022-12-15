# day 13
# Required external verification due to me not understanding everything about the comparisons
# but got part 2 easily after part 1!

import numpy as np


# sample = True
sample = False

if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()


def to_list(line):
    out = []
    lists = []
    curr = out
    parsing_number = False
    
    for s in line: 
        if parsing_number and not s.isdigit():
            number = int("".join(curr))
            curr = lists.pop()
            curr.append(number)
            parsing_number = False
        
        if s.isdigit():
            if not parsing_number:
                parsing_number = True
                lists.append(curr)
                curr = []
            curr.append(s)
        if s == "[":
            # old = curr
            lists.append(curr)
            curr = []
        elif s == "]":
            tmp = curr
            curr = lists.pop()
            curr.append(tmp)

            # lists[0].append(int(s))
    # if len(old) < 2:
    return curr
    # else:
        # return old
lines.append("")
pairs = [] 
curr_pair = []
for i in range(len(lines)):
    if lines[i] == "":
        pairs.append(curr_pair)
        curr_pair = []
    else:
        curr_pair.append(to_list(lines[i]))

def compare_pair(p1, p2):
    for i in range(max(len(p1), len(p2))):
        if i >= len(p2):
            # print(p1, "vs", p2)
            # print("failed due to running out of right")    
            return -1
        if i == len(p1):
            return 1

        if isinstance(p1[i],int) and isinstance(p2[i], int):
            if p1[i] > p2[i]:
                # print(p1, "vs", p2)
                # print("failed due to ", p1[i], "vs", p2[i])
                return -1
            elif p1[i] < p2[i]:
                return 1
        elif isinstance(p1[i], list) and isinstance(p2[i], list):
            res = compare_pair(p1[i], p2[i])
            if res != 0: return res
        else:
            res =  compare_pair([p1[i]] if isinstance(p1[i], int) else p1[i], 
                                [p2[i]] if isinstance(p2[i], int) else p2[i])
            if res != 0: return res
    return 0

corrects = []
def sum_list_of_list(lst):
    total = 0
    for e in lst:
        if isinstance(e, list):
            total += sum_list_of_list(e)
        else:
            total += e
    return total

sum_indices = 0
for i in range(len(pairs)):
    p = pairs[i]
    
    if compare_pair(p[0], p[1]) == 1:
        # print(i,":")
        # print("\t",p[0])
        # print("\t",p[1])
        # print(sum_list_of_list(p[0]), sum_list_of_list(p[1]))
        sum_indices+= i + 1
        # corrects.append(sum_list_of_list(p[0])+ sum_list_of_list(p[1]))
        
print("Num pairs:", len(pairs))
print("Part 1 =", sum_indices)

vals = []
[(vals.append(p[0]), vals.append(p[1])) for p in pairs]
vals.append([[2]])
vals.append([[6]])
# [print(v) for v in vals]

from functools import cmp_to_key
vals.sort(key=cmp_to_key(compare_pair),reverse=True)
# [print(v) for v in vals]

key1 = vals.index([[2]]) + 1 
key2 = vals.index([[6]]) + 1 
decoder_key = key1 * key2 
print("part 2:", decoder_key)
