# 12
import time
import numpy as np
from copy import deepcopy

debug = False
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()


# Loading
if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input2.txt", 'r').read().splitlines()
lines = [l.split("-") for l in lines]
mapping  = {}
for item in lines:
    mapping[item[0]] = set()
    mapping[item[1]] = set()
if debug: [print(name,":", value) for name, value in lines]
[mapping[name].add(value) for [name, value] in lines]

# double-sided
for name, values in mapping.items(): 
    for value in values:
        mapping[value].add(name)

if debug:
    print("Completed Mapping:")
    [print(name,":", value) for name, value in mapping.items()]

##########################################
def part1():
    paths = []
    def DFS(graph, visited, name, path):
        cur_visited = visited.copy()
        cur_visited[name] = True
        # visited[name] = True
        cur_path = path + [name]
        for neighbor in graph[name]:
            if neighbor == "end":
                paths.append("->".join(cur_path+["end"]))
            elif not visited[neighbor] or neighbor.isupper():
                DFS(graph, cur_visited, neighbor, cur_path)

    # base_path = ['start']
    # current_path = base_path.copy()
    # visited = {name: set() for name in mapping.keys()}
    # print(visited)
    # path_stack = []
    # choices = list(mapping[current_path.pop()])
    # while len(choices) > 0:

    paths = []
    visited = {name: False for name in mapping.keys()}
    DFS(mapping, visited, "start", [])

    # print(paths)
    print("Part 1: paths =",len(paths))

########################################## 
def part2():
    paths = []

    def DFS(graph, visited, name, path, doubled_up):
        cur_visited = deepcopy(visited)
        cur_visited[name] = True
        # visited[name] = True
        cur_path = path + [name]
        for neighbor in graph[name]:
            if neighbor == "start":
                continue
            elif neighbor == "end":
                paths.append("->".join(cur_path+["end"]))
            elif not cur_visited[neighbor] or neighbor.isupper():
                DFS(graph, cur_visited, neighbor, cur_path, doubled_up)
            elif not doubled_up:
                DFS(graph, cur_visited, neighbor, cur_path, True)


    paths = []
    visited = {name: False for name in mapping.keys()}
    doubled_up = False
    DFS(mapping, visited, "start", [], doubled_up)

    # print(paths)
    print("Part 2: paths =",len(paths))

part1()
part2()

print("Done")