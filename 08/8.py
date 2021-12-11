# 08
import time


startTime = time.time()

lines = open("input.txt", 'r').read().splitlines()

ins_outs  = [l.split(' | ') for l in lines]
ins_outs = [[side.split(' ') for side in l] for l in ins_outs]

_1, _4, _7, _8 = 0, 0, 0, 0
ds = []
for i in range(len(ins_outs)):
    d = {}
    for code in ins_outs[i][1]:
        digits = len(code)
        if digits == 2:
            _1 += 1
            d[1] = code
        elif digits == 4:
            _4 += 1
            d[4] = code
        elif digits == 3:
            _7 += 1
            d[7] = code
        elif digits == 7:
            _8 += 1
            d[8] = code

print(f"1s={_1} 4s={_4} 7s={_7} 8s={_8};  Total = {_1+_4+_7+_8}  time={time.time()-startTime}s")

def char_intersection(s1, s2):
    return "".join([c for c in s1 if c in s2])

def char_sub(s1, s2):
    return "".join([c for c in s1 if c not in s2])

def char_has_all(s1, s2):
    return all([c in s1 for c in s2])

# test1 = "abcde"
# test2 = "dba"
# test3 = "abj"
# print(char_has_all(test1, test2))
# print(char_has_all(test1, test3))

# exit()
sum = 0 
for i in range(len(ins_outs)):
    d = {}
    for code in ins_outs[i][0]:
        digits = len(code)
        if digits == 2:
            _1 += 1
            d[1] = code
        elif digits == 4:
            _4 += 1
            d[4] = code
        elif digits == 3:
            _7 += 1
            d[7] = code
        elif digits == 7:
            _8 += 1
            d[8] = code
    for code in ins_outs[i][0]:
        digits = len(code)
        if digits in (2,3,4,7):
            continue
        elif digits == 5:
            if char_has_all(code, char_sub(d[4],d[7])):
                d[5] = code
            elif char_has_all(code, char_intersection(d[4],d[7])):
                d[3] = code
            else:
                d[2] = code
        elif digits == 6: # len = 6
            if char_has_all(code, char_sub(d[8],d[1])):
                d[6] = code
            elif char_has_all(code, char_sub(d[4],d[7])):
                d[9] = code
            else:
                d[0] = code
    for rev_place in range(4):
        captured = False
        for key, decode in d.items():
            cur_encode = ins_outs[i][1][rev_place]
            if char_has_all(cur_encode,decode) and char_has_all(decode, cur_encode):
                sum += key * 10 ** (3-rev_place)
                captured = True
                break
        if not captured:
            raise ValueError("Could not find appropriate code!")


print(f"Part 2: Sum={sum} time={time.time()-startTime}s")

# 973292 ???



print("Done")