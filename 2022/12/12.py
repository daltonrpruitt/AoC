# day 12
# had to get help initially. was quite out of it...

import numpy as np
from copy import deepcopy


sample = False

if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

grid = np.array([[ord(c) for c in l] for l in lines], dtype=np.int8)
start = np.array(np.where(grid == ord('S')))[:,0]
end = np.array(np.where(grid == ord('E')))[:,0]

grid[tuple(start)] = ord('a')
grid[tuple(end)] = ord('z')

width = len(lines)
length = len(lines[0])

print(width, "x", length)
print(grid)
print("start=",start," end=",end)

class node():
    parent = None
    child = None
    pos = None
    def __init__(self,pos, n=None) -> None:
        self.pos = pos
        if n is not None:
            self.parent = n
            n.set_child(self)
        
    def set_child(self, n):
        self.child = n
        
    # def __str__(self) -> str:
    #     cur = self
    #     out = "->"+str(self.pos)
    #     while cur.parent is not None:
            
    #     return (str(self.parent) if self.parent is not None else "") + "->" + str(self.pos)

    def __repr__(self) -> str:
        p = self.parent
        out = str(self.pos)
        while p is not None:
            out = str(p.pos) + "->" + out
            p = p.parent
        return out

def bfs():
    
    to_visit = []
    visited = np.zeros(grid.shape)
    # visited_count = 0
    steps = 0
    at_end = False
    # curr = start
    visited[tuple(start)] = True
    to_visit.append(node(start))
    n = None
    
    while not at_end:
        curr_n = to_visit.pop(0)
        
        old_parent = n.parent if n is not None else None
        # n = node(curr, old_parent)
        child = None
        # child = None
        # steps += 1
        for i in ((-1,0),(1,0),(0,-1),(0,1)):
            if curr_n.pos[0] + i[0] >= width or curr_n.pos[0] + i[0] < 0:
                continue
            if curr_n.pos[1] + i[1] >= length or curr_n.pos[1] + i[1] < 0:
                continue
            new_pos = curr_n.pos + np.array(i)
            if visited[tuple(new_pos)]:
                continue
            if grid[tuple(new_pos)] > grid[tuple(curr_n.pos)] + 1:
                continue
            if np.all(new_pos == end):
                # steps += 1
                at_end = True
                new_node = node(new_pos, curr_n)
                return new_node
            to_visit.append(node(new_pos, curr_n))
            visited[tuple(new_pos)] = True
        # old_parent = parent

n = bfs()
print("Part 1")
print("Steps = ",n)
print("steps = ", str(n).count("->"))
print(("#"*90+"\n")*4)

def bfs2():
    
    to_visit = []
    visited = np.zeros(grid.shape)
    # visited_count = 0
    steps = 0
    at_end = False
    # curr = start
    visited[tuple(end)] = True
    to_visit.append(node(end))
    n = None
    
    while not at_end:
        curr_n = to_visit.pop(0)
        
        old_parent = n.parent if n is not None else None
        # n = node(curr, old_parent)
        child = None
        # child = None
        # steps += 1
        for i in ((-1,0),(1,0),(0,-1),(0,1)):
            if curr_n.pos[0] + i[0] >= width or curr_n.pos[0] + i[0] < 0:
                continue
            if curr_n.pos[1] + i[1] >= length or curr_n.pos[1] + i[1] < 0:
                continue
            new_pos = curr_n.pos + np.array(i)
            if visited[tuple(new_pos)]:
                continue
            if grid[tuple(new_pos)] < grid[tuple(curr_n.pos)] - 1:
                continue
            if grid[tuple(new_pos)] == ord('a'):
                # steps += 1
                at_end = True
                new_node = node(new_pos, curr_n)
                return new_node
            to_visit.append(node(new_pos, curr_n))
            visited[tuple(new_pos)] = True
        # old_parent = parent

opt_start = bfs2()
print("Part 2")
print("Steps = ",opt_start)
print("steps = ", str(opt_start).count("->"))
