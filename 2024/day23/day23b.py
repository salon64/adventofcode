from collections import defaultdict
import copy
from itertools import permutations
import itertools
import re
import time
import heapq
import bisect
start_time = time.time()
with open('2024/day23/day_23_input.txt', 'r') as file: # day_23_input.txt
    data = file.read().strip().splitlines()

connections = [line.split('-') for line in data]
computer_connections = defaultdict(set)
# print(connections)
                  
for comp1, comp2 in connections:
    if comp1 != comp2:
        computer_connections[comp1].add(comp2)
        computer_connections[comp2].add(comp1)
# print(computer_connections) 


biggest_network = 0
# cache = {}
def next_connection(curr_comp, path):
    global biggest_network
    all_visited = True
    for connected_comp in computer_connections[curr_comp]:
        if connected_comp not in path:  # Avoid revisiting nodes
            bisect.insort(path, connected_comp) # insert, sorted
            next_connection(connected_comp, path[:])
            all_visited = False
    
    if all_visited:
        biggest_network = max(biggest_network, len(path))



computers = set()
for comps in connections:
    for c in comps:
        computers.add(c)
# print(computers)
for i, comp in enumerate(computers):
    # print(f"{comp},  {[comp]}")
    print(f"{i} of {len(computers)}")
    next_connection(comp, [comp])



print(f"biggest network: {biggest_network}")
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')


# for i, tri in enumerate(tripplets):
#     a, b, c = tri
#     # print(tripplets[i], end="")
#     okay = False
#     if a[0] == 't' or a[-1] == 't':
#         okay = True
#     elif b[0] == 't' or b[-1] == 't':
#         okay = True
#     elif c[0] == 't' or c[-1] == 't':
#         okay = True

#     if okay:
#         tripplets_with_t += 1
#         # print(" okay")
#     else:
#         # print(" not okay")
#         pass