import copy
from itertools import permutations
import re
import time
import heapq
start_time = time.time()
with open('2024/day21/test', 'r') as file: # day_21_input.txt
    data = file.read().strip().splitlines()

codes = [list(line) for line in data]
print(codes)

# ta reda på alla avstånden mellan knapparna


numeric = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2),
}
directional = {
    '^': (0, 0), 'A': (0, 1),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}
# def calculate_distances(layout):
#     distances = {}
#     keys = list(layout.keys())
#     for i, key1 in enumerate(keys):
#         for j, key2 in enumerate(keys):
#             if key1 != key2:  # Skip self-comparison
#                 y1, x1 = layout[key1]
#                 y2, x2 = layout[key2]
#                 y_dist = abs(y1 - y2)
#                 x_dist = abs(x1 - x2)
#                 manhattan_dist = y_dist + x_dist
#                 distances[(key1, key2)] = manhattan_dist
#     return copy.deepcopy(distances)

def calculate_offset(layout):
    distances = {}
    keys = list(layout.keys())
    for i, key1 in enumerate(keys):
        for j, key2 in enumerate(keys):
            if key1 != key2:  # Skip self-comparison
                y1, x1 = layout[key1]
                y2, x2 = layout[key2]
                tmp = ((y1-y2), (x1-x2))
                print(f"{key1} -> {key2}: tmp = {tmp}, type = {type(tmp)}")
                distances[(key1, key2)] = tmp
    return copy.deepcopy(distances)


def calculate_all_shortest_paths(distances, nodes):
    shortest_paths = {}
    for start_node in nodes:
        for target1, target2 in permutations(nodes, 2):  # All pairs of target nodes
            if target1 != start_node and target2 != start_node:
                # Generate both possible visiting orders
                paths = [
                    (start_node, target1, target2),  # Start -> Target1 -> Target2
                    (start_node, target2, target1),  # Start -> Target2 -> Target1
                ]
                
                # Calculate the total distance for each path
                shortest_path = None
                shortest_distance = float('inf')
                for path in paths:
                    total_distance = (
                        distances[(path[0], path[1])] +  # Start -> Target1/Target2
                        distances[(path[1], path[2])]   # Target1/Target2 -> Target2/Target1
                    )
                    if total_distance < shortest_distance:
                        shortest_distance = total_distance
                        shortest_path = path

                # Store just the visiting order (excluding start node) for this combination
                shortest_paths[(start_node, target1, target2)] = shortest_path[1:]  # Exclude the start node
    return shortest_paths


# numeric_distances = calculate_distances(numeric)
# directional_distances = calculate_distances(directional)
# combined_layout = {**numeric_distances, **directional_distances}

numeric_offset = calculate_offset(numeric)
directional_offset = calculate_offset(directional)
combined_offset = {**numeric_offset, **directional_offset}

# shortest_paths = calculate_all_shortest_paths(directional_distances, directional.keys())

# +---+---+---+  #     +---+---+  #     +---+---+
# | 7 | 8 | 9 |  #     | ^ | A |  #     | ^ | A |
# +---+---+---+  # +---+---+---+  # +---+---+---+   user
# | 4 | 5 | 6 |  # | < | v | > |  # | < | v | > |   
# +---+---+---+  # +---+---+---+  # +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

print(numeric_offset)
print(numeric_offset.get('A', '2'))

positions = ['A', 'A', 'A']
def solve(start, end, depth):
    if depth == 3:
        return combined_layout.get(start, end)
    elif depth == 0:
        # find closest button from cur button, press it, move to next closest one then press that
        solve()
    
# for code

# result = 0
# for code in codes:
#     tmp = 0
#     for char in code:
#         tmp += solve(positions[0], char, 0)
#     print(tmp)
#     tmp2 = int(str("".join(code)))
#     result += tmp * tmp2


end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

