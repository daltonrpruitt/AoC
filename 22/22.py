# 22
# Part 2 based on https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hqxczc4/?utm_source=share&utm_medium=web2x&context=3

import time
import numpy as np

debug = True
sample = False
def debug_log(output):
    if debug: print(output)

class Operation(object):
    def __init__(self, setting, ranges):
        xs, ys, zs = ranges
        self.setting = setting
        self.x = [min(xs), max(xs)]
        self.y = [min(ys), max(ys)]
        self.z = [min(zs), max(zs)]
        assert self.x[0] <= self.x[1]
        assert self.y[0] <= self.y[1]
        assert self.z[0] <= self.z[1]
    def __repr__(self):
        return f"Set {self.x},{self.y},{self.z} to "+setting

startTime = time.time()

filename = "sample_input.txt" if sample else "input.txt"
lines = open(filename, 'r').read().splitlines()

operations = []
for line in lines:
    setting, ranges = line.split(" ")
    operations.append(Operation(setting, 
    [[int(val) for val in axis[1].split("..")] for axis in [r.split("=") for r in ranges.split(",")]]))

def output_lights(lights, i):
    sh = lights.shape
    np.savetxt(f"lights_{sh[0]}x{sh[1]}x{sh[2]}_{i}.txt", np.reshape(lights, newshape=(sh[0]*sh[1],sh[2])), fmt='%d')

# State:
#    0: indeterminate
#    1: must be on
#    2: must be off
sz = 50
size = sz - -sz + 1
print(size)
lights = np.zeros(shape=(size,size,size), dtype=int)
# lights += 10

def translated_operation(o, trans):
    values = [[i+trans for i in a] for a in [o.x,o.y,o.z]]
    translated = Operation(o.setting, values)
    return translated

def check_done(lights):
    yet_to_set = lights == 0
    if yet_to_set.sum().sum().sum() == 0:
        return True
    else:
        return False
    
def set_range(lights, op):
    if (op.x[1]+1 < 0 or op.x[0] > size or \
        op.y[1]+1 < 0 or op.y[0] > size or \
        op.z[1]+1 < 0 or op.z[0] > size): return lights

    xs = np.intersect1d(np.arange(op.x[0], op.x[1]+1), np.arange(size+1))
    ys = np.intersect1d(np.arange(op.x[0], op.y[1]+1), np.arange(size+1))
    zs = np.intersect1d(np.arange(op.z[0], op.z[1]+1), np.arange(size+1))
    # print("Intersection of", op.x, op.y, op.z)
    # print("and "+("[0,"+str(lights.shape[0])+"]")*3 +" = ")
    # print(xs, ys, zs, sep="\n")
    can_set = np.zeros(shape=lights.shape,dtype=int)
    if len(xs) == 0 or len(ys) == 0 or len(zs) == 0:
        return lights
    # can_set[xs[0]:xs[-1],ys[0]:ys[-1],zs[0]:zs[-1]] = lights[xs[0]:xs[-1],ys[0]:ys[-1],zs[0]:zs[-1]] == 0

    # if can_set.sum().sum().sum() > 0:
    val = 1 if op.setting == "on" else 2
    # print(can_set)
    # lights[xs[0]:xs[-1],ys[0]:ys[-1],zs[0]:zs[-1]]  = \
    #     (1 - can_set[xs[0]:xs[-1],ys[0]:ys[-1],zs[0]:zs[-1]]) * lights[xs[0]:xs[-1],ys[0]:ys[-1],zs[0]:zs[-1]] + \
    #         can_set[xs[0]:xs[-1],ys[0]:ys[-1],zs[0]:zs[-1]] * val
    for i in xs:
        for j in ys:
            for k in zs:
                # if can_set[i,j,k] ==1:
                lights[i,j,k] = val

    # print(lights[xs,ys,zs])

    return lights

if False:
    i = 0
    for o in operations:
        trans_o = translated_operation(o, sz)
        lights = set_range(lights, trans_o)
        i+= 1
        # output_lights(lights, i)
        if check_done(lights): 
            print("Finished!")
            break

    # lights2 = np.zeros(shape=(size,size,size))
    # for o in operations:
    #     lights2 = set_range(lights2, translated_operation(o,sz))

    # num_lit = (lights2==1).sum().sum().sum()
    # print(f"Part 1: Num Lights ={num_lit} Time={time.time()-startTime}s")
    # exit()

    if not check_done(lights):
        print("Failed!")
        print("Num set =", (lights != 0).sum().sum().sum())
        print("Num not set =", (lights == 0).sum().sum().sum())

    num_lit = (lights==1).sum().sum().sum()
    print(f"Part 1: Num Lights = {num_lit} Time={time.time()-startTime}s")
    # 628523 too high
    # 466252 too low 
    # 485896 too low
    # 551693

def basic_part1(ops):
    lights = set()

    for op in ops:
        if (op.x[1] < -sz or op.x[0] > sz or \
            op.y[1] < -sz or op.y[0] > sz or \
            op.z[1] < -sz or op.z[0] > sz):
            continue
        for x in range(max(op.x[0],-sz), min(op.x[1],sz)+1):
            for y in range(max(op.y[0],-sz), min(op.y[1],sz)+1):
                for z in range(max(op.z[0],-sz), min(op.z[1],sz)+1):
                    if op.setting == "on":
                        lights.add((x,y,z))
                    else:
                        lights.discard((x,y,z))
    
    print(f"Part 1 (basic): Num Lights = {len(lights)} Time={time.time()-startTime}s")

basic_part1(operations)


class Cuboid(object):
    def __init__(self, setting=None, xs=None, ys=None, zs=None, operation=None):
        if operation is None:
            xs = (min(xs), max(xs))
            ys = (min(ys), max(ys))
            zs = (min(zs), max(zs))
            self.x, self.y, self.z = xs, ys, zs 
            self.setting = setting
        else:
            self.x, self.y, self.z = operation.x, operation.y, operation.z
            self.setting = 1 if operation.setting == "on" else 0
    
    def intersection(self, other):
        assert isinstance(other, Cuboid)
        inter_xs = (max(self.x[0], other.x[0]), min(self.x[1], other.x[1]))
        inter_ys = (max(self.y[0], other.y[0]), min(self.y[1], other.y[1]))
        inter_zs = (max(self.z[0], other.z[0]), min(self.z[1], other.z[1]))
        if (inter_xs[0] > inter_xs[1] or
            inter_ys[0] > inter_ys[1] or
            inter_zs[0] > inter_zs[1]):
            return None
        return Cuboid(-other.setting, inter_xs, inter_ys, inter_zs)

    def signed_volume(self):
        return self.setting * (self.x[1]-self.x[0]+1) * (self.y[1]-self.y[0]+1) * (self.z[1]-self.z[0]+1)

# based on https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hqxczc4/?utm_source=share&utm_medium=web2x&context=3
set_cuboids = []
for o in operations:
    new_cube = Cuboid(operation=o)
    cubes_to_add = [new_cube] if o.setting == "on" else []
    for c in set_cuboids:
        inter = new_cube.intersection(c)
        if inter:
            cubes_to_add.append(inter)
    set_cuboids += cubes_to_add

count = 0
for c in set_cuboids:
    count += c.signed_volume()
print("Total lights for part 2:", count, round(time.time()-startTime,2), "s")
# 1165737675582132 