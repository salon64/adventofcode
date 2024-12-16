import time
from collections import defaultdict, deque as queue
start_time = time.time()
with open('2024/day16/day_16_input.txt', 'r') as file: # day_16_input.txt
    data = file.read().strip().splitlines()

pos = (0, 0)
data = [list(line) for line in data]
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == 'S':
            pos = (y, x)
            break

distances = {}
def is_valid(y, x, new_dist):
    if (y, x) in distances and distances[(y, x)] <= new_dist:
        return False
    return data[y][x] != '#'

q = queue()
q.append((pos[0], pos[1], 1, 0))  # (y, x, direction, distance)
distances[(pos[0], pos[1])] = 0
ends = []

while (len(q) > 0):
    y, x, dir, dist = q.popleft()
    distances[(y, x)] = dist
    if data[y][x] == 'E':
        ends.append(dist)
    
    for dy, dx, new_dir in [(-1, 0, 0), (1, 0, 2), (0, 1, 1), (0, -1, 3)]:  # (dy, dx, direction)
        ny, nx = y + dy, x + dx
        turn_penalty = min(abs(dir - new_dir), 4 - abs(dir - new_dir)) * 1000
        new_dist = dist + 1 + turn_penalty
        if is_valid(ny, nx, new_dist):
            q.append((ny, nx, new_dir, new_dist))

ends.sort()
print(ends[0])
    
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
