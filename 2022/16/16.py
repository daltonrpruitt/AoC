# day 16
# had to get help initially. was quite out of it...

import numpy as np
from copy import deepcopy


sample = True
# sample = False

if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

# "valve0" : {"pressure": val, "connections": ["valve1", "valve2", etc.] }
graph = {}

for ln in lines:
    l,r = ln.split(" has flow rate=")
    v = l[len("Valve "):]
    flow = int(r[:r.find(";")])
    next_vs = r.split(", ")
    next_vs[0] = next_vs[0][-2:]
    print(next_vs)
    
    graph[v] = {"pressure":flow, "opened":False, "connections": next_vs}
    
for key in graph.keys():
    print(key, graph[key])


time_left = 30
max_time = 30

    
def update_effective_values(graph, eff_val_graph, node, time_left, remove=False):

    press = graph[node]["pressure"]
    if press == 0:
        return
    
    if remove:
        press *= -1

    is_visited = {k:False for k in graph.keys()}
    # unvisited = [k for k in graph.keys()]
    # is_visited[node] = True
    # unvisited.remove(node)
    # if remove: eff_val_graph[node]["val"] = 0
    
    # max_found = max([eff_val_graph[i]["val"] for i in graph[node]["connections"]])
    eff_val_graph[node]["val"] += (press*1.5 if remove else press)*(time_left) #max(eff_val_graph[node]["val"], max_found)

    is_visited[node] = True
    # dist = 29
    next_layer = set()
    curr_layer = set(graph[node]["connections"])
    for i in range(1, time_left):
        if len(curr_layer) == 0: break
        for c in curr_layer:
            if is_visited[c] or c in eff_val_graph[c]["visited"] :
                continue
            # max_found = max([eff_val_graph[i]["val"] for i in graph[c]["connections"]])
            eff_val_graph[c]["val"] += press*(time_left-i) #+ max(0, max_found)

            # eff_val_graph[c]["val"] = max((time_left - i) * press, eff_val_graph[c]["val"])
            next_layer |= set(graph[c]["connections"])
            is_visited[c] = True
        curr_layer = deepcopy(next_layer)
        next_layer.clear()

def calculate_effective_values(graph, time_left=max_time):
    effective_vals = {key:{"val":0, "visited":[]} for key in graph.keys()}    
    
    for start in graph.keys():
        update_effective_values(graph, effective_vals, start, time_left)
    return effective_vals

# eff_vals = calculate_effective_values(graph=graph, time_left=max_time)

# for key in eff_vals.keys():
#     print(key, eff_vals[key])

def best_total_value(graph, start):
    time = 0
    # at_end = lambda time: time >= max_time
    
    # start at first valve
    node = start
    # while have time:
    
    eff_vals = calculate_effective_values(graph=graph, time_left=max_time)
    for key in eff_vals.keys():
        print(key, eff_vals[key])
        
    curr_open = 0
    total_val = 0
    last_node = node
    while time <= max_time:
        
        max_eff = 0
        max_node = None
        for c in graph[node]["connections"]:
            if eff_vals[c]["val"] > max_eff and not (c == last_node and graph[c]["pressure"] == 0):
                max_node = c
                max_eff = eff_vals[c]["val"]

        if (not graph[node]["opened"] 
            and graph[node]["pressure"] > 0 
            and (max_eff <= eff_vals[node]["val"] )): # or graph[max_node]["pressure"] == 0) ):
            time += 1
            total_val += curr_open
            curr_open += graph[node]["pressure"]
            graph[node]["opened"] =  True
            print("Opened valve '"+ node+"'")
            update_effective_values(graph, eff_vals, node, time_left=max_time-time, remove=True)
        
        # if graph[node]["pressure"] == 0:
        #     max_eff = 0
        #     max_node = None
        #     for c in graph[node]["connections"]:
        #         if eff_vals[c]["val"] > max_eff and graph[c]["pressure"] > 0:
        #             max_node = c
        #             max_eff = eff_vals[c]["val"]
        
        time += 1
        total_val+=curr_open
        print("Moved from '"+ node+"' to '"+ max_node+"'")
        last_node = node
        node = max_node

    return total_val
    # max_connection = find max unopened connection
    # if max_connection <= curr value:
    #    open current valve (time+=1)
    # 
val = best_total_value(graph, "AA")

print("Part 1:", val)

