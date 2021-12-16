# 15
import time
import numpy as np

debug = True
full_debug = False
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()


# Loading
if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

lines = [" ".join([c for c in l]) for l in lines]
lines = [np.fromstring(l,dtype=int,sep=" ") for l in lines] 
risks = np.stack(lines, axis=0)

# print(risks[:10,:10])

path = [risks[-1,-1]]
size = risks.shape[0]
paths_completed = 0
min_cost_seen = np.inf

def filled_risk_matrix(risks_mat):
    total_risks = 10**5 * np.ones(risks_mat.shape, dtype=int)
    # total_risks[0,:] = risks_mat[0,:]
    # total_risks[:,0] = risks_mat[:,0]
    # print(total_risks[1,:10])

    total_risks[0,0] = 0
    for i in range(1, risks_mat.shape[0]):
        total_risks[0,i] =  total_risks[0,i-1] + risks_mat[0,i]
        total_risks[i,0] =  total_risks[i-1,0] + risks_mat[i,0]
    print(total_risks[:5,:5])

    for i in range(1,risks_mat.shape[0]):
        for j in range(1, risks_mat.shape[0]):
            total_risks[i,j] = min(total_risks[i-1,j], total_risks[i,j-1]) + risks_mat[i,j]

    return total_risks


def generate_larger_risk_matrix(risk_mat):
    sz = risk_mat.shape[0]
    output_mat = np.zeros(shape=(sz*5, sz*5), dtype=int)
    output_mat[0:sz, 0:sz] = risk_mat
    for i in range(0,5):
        for j in range(0,5):
            total_extra = i + j
            if total_extra == 0: continue
            output_mat[sz*i:sz*(i+1), sz*j:sz*(j+1)] = np.mod(risk_mat + total_extra-1, 9) + np.ones(shape=risk_mat.shape)
            if debug and full_debug:
                print("At ",i,",",j)
                print(risk_mat[:5,:5])
                print(output_mat[sz*i:sz*i+5, sz*j:sz*j+5])
                exit()
    if debug:
        # print("Compare original mat to what it should be + 8 (or -1)")
        # print(risk_mat[:10,:10])
        # print(output_mat[sz*4:sz*4+10, sz*4:sz*4+10])
        print(output_mat[10::sz,10::sz])
    return output_mat

def part1_attempt2():
    computed_risks = filled_risk_matrix(risks) 
    if debug:
        print(computed_risks[-10:,-10:])

    print(f" risk ={computed_risks[-1,-1]} Time={time.time() - startTime}s")
    np.savetxt("output_risks.txt", computed_risks, fmt="%d")

def find_path(base_risks, total_risks):
    i = j  = total_risks.shape[0]-1
    path = [(i,j)]
    while i > 0 and j > 0:
        up = total_risks[i-1,j] 
        left = total_risks[i,j-1] 
        if up < left:
            path.insert(0, (i-1,j))
            i -= 1
        else:
            path.insert(0, (i,j-1))
            j -= 1

    if i>0:
        for x in range(i-1,0,-1):
            path.insert(0, (x,0))
    else:
        for x in range(j-1,0,-1):
            path.insert(0, (0,x))
    return path

def output_path(vals, path, size):
    with open("output_path_"+str(size)+".txt",'w') as f:
        for i in range(size):
            for j in range(size):
                if (i,j) in path or (i==0 and j==0): f.write(str(vals[i,j]))
                else: f.write("-")
            f.write("\n")
        

def part2():
    larger_matrix = generate_larger_risk_matrix(risks)
    larger_input_filename = "input_risks_larger"
    if sample: larger_input_filename += "_sample"
    np.savetxt(larger_input_filename+".txt", larger_matrix, fmt="%d")
    # exit()
    computed_risks = filled_risk_matrix(larger_matrix) 
    sz = risks.shape[0]
    if debug:
        print("Samples of computed risks:")
        print(computed_risks[:10,:10])
        print(computed_risks[sz-5:sz+5,sz-5:sz+5])
        print(computed_risks[-10:,-10:])

    print(f"Part 2 risk = {computed_risks[-1,-1]} Time={time.time() - startTime}s")
    larger_output_filename = "output_risks_larger"
    if sample: larger_output_filename += "_sample"

    np.savetxt(larger_output_filename+".txt", computed_risks, fmt="%d")
    found_path = find_path(larger_matrix, computed_risks)
    print(found_path)
    print(f"Path length = {len(found_path)}")
    output_path(larger_matrix,found_path, sz*5)

part1_attempt2() 
# 442 is too high
# ... -7 from the starting point....
# 435 is the right answer!

part2()
# 2846 too high (but is the correct answer for someone else... well, idk man. I haven't used someone's answer)

print("Done")










def dfs(x=0, y=0, cur_cost=0):
    global min_cost_seen
    global paths_completed

    if paths_completed % 1000 == 999:
        if debug:print(f"Completed {paths_completed+1} paths in {time.time() - startTime}s")

    local_cost = cur_cost
    if local_cost >= min_cost_seen:
        paths_completed += 1
        return np.inf
    if x >= size-1 and y >= size-1:
        min_cost_seen = local_cost
        paths_completed += 1
        return local_cost
    elif x >= size-1:
        return dfs(x, y+1, local_cost + risks[x,y+1])
    elif y >= size-1:
        return dfs(x+1, y, local_cost + risks[x+1,y])
    else:
        if risks[x+1, y] < risks[x, y+1]:
            return min(
                dfs(x+1, y, local_cost + risks[x+1, y]),
                dfs(x, y+1, local_cost + risks[x, y+1])
            )
        else:
              return min(
                dfs(x, y+1, local_cost + risks[x, y+1]),
                dfs(x+1, y, local_cost + risks[x+1, y])
            )
def part1_attempt():
    res = dfs() 
    print(res)

    print(f" risk ={res} Time={time.time() - startTime}s")
