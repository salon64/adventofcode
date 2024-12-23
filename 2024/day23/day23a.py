from collections import defaultdict
import time
start_time = time.time()
with open('2024/day23/day_23_input.txt', 'r') as file: # day_23_input.txt
    data = file.read().strip().splitlines()

connections = [line.split('-') for line in data]
computer_connections = defaultdict(set)
                  
for comp1, comp2 in connections:
    if comp1 != comp2:
        computer_connections[comp1].add(comp2)
        computer_connections[comp2].add(comp1)

tripplets = set()
def next_connection(curr_comp, path):
    if len(path) == 3: # 3 comps need to be connected
        if path[0] in computer_connections[path[1]] and path[1] in computer_connections[path[2]] and path[2] in computer_connections[path[0]]: # see that all connects to all
            normalized_path = tuple(sorted(path))  # Sort the path and convert it to a tuple
            if normalized_path not in tripplets:
                tripplets.add(normalized_path)
        return
    else:
        for connected_comp in computer_connections[curr_comp]:
            if connected_comp not in path:  # Avoid revisiting nodes
                next_connection(connected_comp, path + [connected_comp])

computers = set()
for comps in connections:
    for c in comps:
        computers.add(c)
for comp in computers:
    next_connection(comp, [comp])

tripplets_with_t = sum(1 for tri in tripplets if any(comp.startswith('t') for comp in tri))
print(tripplets_with_t)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')