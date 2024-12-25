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
# expected moves fore 029A, len = 68
print(len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"))

# ta reda på alla avstånden mellan knapparna

#   terminal             r1               r2                    user
# +---+---+---+  #     +---+---+  #     +---+---+              +---+---+
# | 7 | 8 | 9 |  #     | ^ | A |  #     | ^ | A |              | ^ | A |
# +---+---+---+  # +---+---+---+  # +---+---+---+   user:  +---+---+---+
# | 4 | 5 | 6 |  # | < | v | > |  # | < | v | > |          | < | v | > | 
# +---+---+---+  # +---+---+---+  # +---+---+---+          +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

numeric = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2),
}
directional = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}
def calculate_distances(layout):
    distances = {}
    keys = list(layout.keys())
    for i, key1 in enumerate(keys):
        for j, key2 in enumerate(keys):
            if key1 != key2:  # Skip self-comparison
                y1, x1 = layout[key1]
                y2, x2 = layout[key2]
                y_dist = abs(y1 - y2)
                x_dist = abs(x1 - x2)
                manhattan_dist = y_dist + x_dist
                distances[(key1, key2)] = manhattan_dist
    return distances

def calculate_offset(layout):
    distances = {}
    keys = list(layout.keys())
    for i, key1 in enumerate(keys):
        for j, key2 in enumerate(keys):
            if key1 != key2:  # Skip self-comparison
                y1, x1 = layout[key1]
                y2, x2 = layout[key2]
                tmp = ((y2-y1), (x2-x1))
                # print(f"{key1} -> {key2}: tmp = {tmp}, type = {type(tmp)}")
                distances[(key1, key2)] = tmp
    return distances



numeric_distances = calculate_distances(numeric)
directional_distances = calculate_distances(directional)
numeric_offsets = calculate_offset(numeric)
directional_offsets = calculate_offset(directional)
# print(numeric_offsets[('2', '9')])


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
                shortest_paths[(start_node, target1, target2)] = shortest_path[:]  # Exclude the start node
    return shortest_paths


combined_layout = {**numeric_distances, **directional_distances}
combined_offset = {**numeric_offsets, **directional_offsets}

# print("--")
# print(combined_offset[('2', '9')])
# print(combined_layout[('2', '9')])

shortest_paths = calculate_all_shortest_paths(directional_distances, directional.keys())

#   terminal             r1               r2                    user
# +---+---+---+  #     +---+---+  #     +---+---+              +---+---+
# | 7 | 8 | 9 |  #     | ^ | A |  #     | ^ | A |              | ^ | A |
# +---+---+---+  # +---+---+---+  # +---+---+---+   user:  +---+---+---+
# | 4 | 5 | 6 |  # | < | v | > |  # | < | v | > |          | < | v | > | 
# +---+---+---+  # +---+---+---+  # +---+---+---+          +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

def get_order(origin, up, down, right, left):
    if up and right:
        key = (origin, '^', '>')
    elif up and left:
        key = (origin, '^', '<')
    elif down and right:
        key = (origin, 'v', '>')
    elif down and left:
        key = (origin, 'v', '<')
    else:
        return ('-1', '-1', '-1')  # No valid paths

    if key in shortest_paths:
        return shortest_paths[key]
    else:
        print(f"Key {key} missing in shortest_paths.")
        return ('-1', '-1', '-1')

positions = ['A', 'A', 'A']
def solve(start, end, depth):
    val = 0
    def press():
        # distance between this_robots_pos and A 
        tmp =  solve(positions[depth], 'A', depth+1)
        positions[depth] = 'A'
        return tmp
        

    if depth == len(positions):
        # distancen mellan tidigare loops positioner + 1
        print(combined_layout[(start, end)] + 1, end="")
        print(f": {start} -> {end}")
        return (combined_layout[(start, end)] + 1) # move to pos and press it
    elif start == end:
        val += solve(positions[depth], 'A', depth+1)
        
    elif depth == len(positions)-1:
        off = combined_offset[start, end]
        print(f"depth: {depth}, {start} -> {end}, off: {off}", end="")
        y, x = off
        up = True if y < 0 else False
        down = True if y > 0 else False
        right = True if x > 0 else False
        left = True if x < 0 else False 
        print(f"  up:{up}, down:{down}, right:{right}, left:{left}")
        order = get_order(start, up, down, right, left) 

        if order[0] == '-1': # only one direction is ok 
            if up:
                val += solve(positions[depth], '^', depth+1)
                positions[depth] = '^'
            elif down:
                val += solve(positions[depth], 'v', depth+1)
                positions[depth] = 'v'
            elif right:
                val += solve(positions[depth], '>', depth+1)
                positions[depth] = '>'
            elif left:
                val += solve(positions[depth], '<', depth+1)
                positions[depth] = '<'
        else:
            val += solve(positions[depth], order[1], depth+1)
            positions[depth] = order[1]
            val += solve(positions[depth], order[2], depth+1)
            positions[depth] = order[2]
    else:
        off = combined_offset[start, end]
        print(f"depth: {depth}, {start} -> {end}, off: {off}", end="")
        y, x = off
        up = True if y < 0 else False
        down = True if y > 0 else False
        right = True if x > 0 else False
        left = True if x < 0 else False 
        print(f"  up:{up}, down:{down}, right:{right}, left:{left}")
        order = get_order(start, up, down, right, left) 

        if order[0] == '-1': # only one direction is ok 
            if up:
                val += solve(positions[depth], '^', depth+1)
                positions[depth] = '^'
                val += press()
            elif down:
                val += solve(positions[depth], 'v', depth+1)
                positions[depth] = 'v'
                val += press()
            elif right:
                val += solve(positions[depth], '>', depth+1)
                positions[depth] = '>'
                val += press()
            elif left:
                val += solve(positions[depth], '<', depth+1)
                positions[depth] = '<'
                val += press()
        else:
            # print("dubble")
            val += solve(positions[depth], order[1], depth+1)
            positions[depth] = order[1]
            val += press()

            val += solve(positions[depth], order[2], depth+1)
            positions[depth] = order[2]
            val += press()

    return val
        

result = 0
for code in codes:
    tmp = 0
    for char in code:
        print(f"char: {char} -----------------------------------------------------------------------------------")
        tmp += solve(positions[0], char, 0) # send in start and end 
        pass
    print(tmp)
    comb = ''.join(code)
    tmp2 = int(re.search(r'\d+', comb).group())
    print(tmp2)
    result += tmp * tmp2

print(result)
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

