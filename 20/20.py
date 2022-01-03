# 20
import time
import numpy as np

debug = False
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()

def get_image():
    # Loading
    filename = "sample_input.txt" if sample else "input.txt"
    lines = open(filename, 'r').read().splitlines()

    guide = lines[0]

    image = lines[2:]

    image_mat = np.asarray([[1 if i == "#" else 0 for i in line] for line in image],dtype=int)
    return guide, image_mat

w = 5
def expand_image(guide, image, count):
    flip_fill = guide[0] == "#" and guide[-1] ==  "."
    
    old_shape = image.shape
    new_shape = (old_shape[0]+w*2, old_shape[1]+w*2)
    
    old_image_expanded = np.zeros(shape=new_shape,dtype=int)
    if flip_fill and count % 2 == 0: 
        old_image_expanded[:w,:] = 1
        old_image_expanded[-w:,:] = 1
        old_image_expanded[:,:w] = 1
        old_image_expanded[:,-w:] = 1

    old_image_expanded[w:-w,w:-w] += image
    # if flip_fill and count % 2 == 0: 
    #     output_image(old_image_expanded,"test_count="+str(count)+".txt")
        # exit()

    new_image = np.zeros(shape=new_shape,dtype=int)
    mult_mat = np.reshape(np.array([2**i for i in range(8,-1,-1)], dtype=int),newshape=(3,3))
    # output_image(old_image_expanded, "test1.txt")

    filename = "delete.txt"
    if debug: filename = "test"+str(old_shape)+"_to_"+str(new_shape)+".txt"
    with open(filename,"w") as f:
        for i in range(w-1,new_shape[0]-w+1):
            for j in range(w-1,new_shape[1]-w+1):
                window = old_image_expanded[i-1:i+2, j-1:j+2]
                val = np.multiply(window, mult_mat).sum().sum()
                char = guide[val]
                if debug: f.write(char)
                new_image[i,j] = 1 if guide[val] == "#" else 0
            if debug: f.write('\n')
            
    
    return new_image[w-1:-w+1, w-1:-w+1]

def output_image(image, filename):
    with open(filename, "w") as f:    
        for row in image[:]:
            for val in row:
                f.write("#" if val == 1 else ".")
            f.write("\n")

def part1(guide, image):
    # debug_log("Start")
    # debug_log(image)

    for i in range(2):
        image = expand_image(guide, image, i+1)
        # debug_log(image)
        # output_image(image, "test_enhanced_count="+str(i+1)+".txt")

    filename = ("enhanced" if not sample else "sample_enhanced")+"x2"+".txt"
    output_image(image, filename)
    print(f"Part 1: Num of lit pixels = {image.sum().sum()} ")

def part2(guide, image):
    for i in range(50):
        image = expand_image(guide, image, i+1)
    filename = ("enhanced" if not sample else "sample_enhanced")+"x50"+".txt"
    output_image(image, "modified_"+filename)
    print(f"Part 2: Num of lit pixels = {image.sum().sum()} ")

if __name__ == '__main__':
    guide, image = get_image()

    part1(guide, image)
    print(f"Time = {time.time()-startTime}s")
    # 5985 too high
    # 5565 too low
    # 5583 ?

    part2(guide, image)
    print(f"Time = {time.time()-startTime}s")
    # 19592 ?  

