import time
from collections import defaultdict, deque as queue
start_time = time.time()
with open('2024/day16/test', 'r') as file: # day_16_input.txt
    data = file.read().strip().splitlines()

pos = (0, 0)
end_pos = (0, 0)
distances = {}
source_nodes = defaultdict(list)

data = [list(line) for line in data]
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == 'S':  # Start position
            pos = (y, x)
        elif char == 'E':
            end_pos = (y, x)

def is_valid(y, x, new_dist, oy, ox):
    if (y, x) in distances:
        existing_dist = distances[(y, x)]
        if abs(existing_dist - new_dist) == 1000:
            source_nodes[(y, x)].append((oy, ox))
            return False
        elif existing_dist < new_dist:
            return False
        elif existing_dist > new_dist:
            source_nodes[(y, x)] = [(oy, ox)]
    else:
        distances[(y, x)] = new_dist
        source_nodes[(y, x)] = [(oy, ox)]
    return data[y][x] != '#'  # Not a wall

q = queue()
q.append((pos[0], pos[1], 1, 0))  # (y, x, direction, distance)
distances[(pos[0], pos[1])] = 0
shortest_path_length = float('inf')
while (len(q) > 0):
    y, x, dir, dist = q.popleft()
    if data[y][x] == 'E':
        shortest_path_length = min(shortest_path_length, dist)
        continue

    for dy, dx, new_dir in [(-1, 0, 0), (1, 0, 2), (0, 1, 1), (0, -1, 3)]:  # (dy, dx, direction)
        ny, nx = y + dy, x + dx
        turn_penalty = min(abs(dir - new_dir), 4 - abs(dir - new_dir)) * 1000
        new_dist = dist + 1 + turn_penalty

        if is_valid(ny, nx, new_dist, y, x):
            distances[(ny, nx, dir)] = new_dist
            q.append((ny, nx, new_dir, new_dist))


res = set()
res.add(end_pos)
q2 = queue()
q2.append(end_pos)
while q2:
    origin = q2.popleft()
    if origin == pos:
        res.add(origin)  # Always add the start position once it's reached
    for source in source_nodes[origin]:
        if source not in res:  # Avoid adding already processed nodes
            res.add(source)
            q2.append(source)

for y, x in res:
    data[y][x] = 'O'
for line in data:
    print("".join(line))

    
print(f"shortest path: {shortest_path_length}")
print(len(res))
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')