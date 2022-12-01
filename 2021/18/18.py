# 18
import time
import numpy as np

debug = False
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()


# Loading
if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input4.txt", 'r').read().splitlines()

print(lines)
###################################

def explode(sf_num):
    too_deep = sf_num[1] == 5
    if not np.any(too_deep):
        return sf_num, True
    if debug:
        print(sf_num)
        print("Must Explode!!!!")

    new_sum = sf_num
    left = list(too_deep).index(True)
    right = left + 1
    if left != 0:
        new_sum[0][left-1] += new_sum[0][left]
    if right != len(too_deep) - 1:
        new_sum[0][right+1] += new_sum[0][right]
    inserted = np.asarray((0,4))
    debug_log(inserted)
    # if left == 0: left += 1
    # if right == len(too_deep)-1: right -= 1
    # debug_log(new_sum[:,:left],inserted[:,np.newaxis], new_sum[:,right+1:], sep="\n")
    concatenated = np.empty((2,0), dtype=int)

    # if left !=0: 
    concatenated = np.concatenate((concatenated, new_sum[:,:left]), axis=1)
    
    concatenated = np.concatenate((concatenated, inserted[:,np.newaxis]), axis=1)
    
    # if right != len(too_deep) - 1: 
    concatenated = np.concatenate((concatenated, new_sum[:,right+1:]), axis=1)
    
    new_sum = concatenated #np.concatenate((new_sum[:,:left-1], inserted[:,np.newaxis], new_sum[:,right+1:] ), axis=1)
    debug_log(new_sum)
    return new_sum, False

def split(sf_num):
    too_large = sf_num[0] >= 10
    if not np.any(too_large):
        return sf_num, True
    debug_log(sf_num)
    debug_log("Must Split!!!!")

    idx = list(too_large).index(True)
    val = sf_num[0,idx]
    new_lvl = sf_num[1,idx] + 1
    inserted = np.asanyarray([[val//2, (val+1)//2],[new_lvl, new_lvl]],dtype=int)

    new_sum = np.concatenate((sf_num[:,:idx], inserted, sf_num[:,idx+1:]),axis=1) 
    debug_log(new_sum)

    return new_sum, False

def score(sf_num):
    cur_set = sf_num
    for lvl in range(4, 0, -1):
        keep_going = True
        at_lvl = cur_set[1] == lvl
        if not np.any(at_lvl): continue
        while True:
            left = list(at_lvl).index(True)
            right = left + 1
            val = cur_set[0,left] * 3 + cur_set[0,right] * 2
            inserted = np.asarray([[val],[lvl-1]],dtype=int)

            cur_set = np.concatenate((cur_set[:,:left], inserted, cur_set[:,right+1:]),axis=1) 

            at_lvl = cur_set[1] == lvl
            if not np.any(at_lvl): break
        if len(cur_set) == 1:
            break
    return cur_set[0,0]




####################################

sf_nums = []
for l in lines:
    new_sf_num = [[],[]]
    d = 0
    for i in range(len(l)): 
        if l[i] == "[":
            d += 1
        elif l[i] == "]":
            d -= 1
        if l[i].isdigit():
            num = l[i]
            if l[i+1].isdigit():
                num += l[i+1]
            new_sf_num[0].append(int(num))
            new_sf_num[1].append(d)
    sf_nums.append(np.asarray(new_sf_num,dtype=int))


def part1(num_list):
    cur_sum = num_list[0]
    for n in num_list[1:]:
        new_sum =  np.concatenate((cur_sum, n),axis=1)
        new_sum[1] += 1

        while True:
            good = False

            new_sum, good = explode(new_sum)
            if not good: continue

            new_sum, good = split(new_sum)
            if good: break

        cur_sum = new_sum.copy()

    print("Output SF #:")
    print(cur_sum)
    scr = score(cur_sum)
    # [print(i) for i in sf_nums]

    # part 1
    print(f"Value = {scr} Time={time.time() - startTime}s") # 4116

def part2(num_list):
    cur_max = 0
    for i in num_list:
        for j in num_list:
            if len(i[0]) == len(j[0]):
                if (i - j)[0].sum() == 0: continue
            new_sum =  np.concatenate((i, j),axis=1)
            new_sum[1] += 1

            while True:
                good = False

                new_sum, good = explode(new_sum)
                if not good: continue

                new_sum, good = split(new_sum)
                if good: break
            scr = score(new_sum)
            cur_max = max(cur_max, scr)


    # part 2
    print(f"Max = {cur_max} Time={time.time() - startTime}s") # 4638


part1(sf_nums)
part2(sf_nums)