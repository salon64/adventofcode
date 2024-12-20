import copy
import re
import time
import heapq
start_time = time.time()
with open('2024/day20/day_20_input.txt', 'r') as file: # day_20_input.txt
    data = file.read().strip().splitlines()

grid = [list(row) for row in data]
start, end = None, None

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'S':
            start = (y, x)
        elif char == 'E':
            end = (y, x)

height, width = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_shortest_path():
    pq = [(0, start[0], start[1])]  # (distance, y, x)
    distances = {start: 0}

    while pq:
        current_dist, y, x = heapq.heappop(pq)

        if (y, x) == end:
            return current_dist

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] != '#':
                new_dist = current_dist + 1
                if (ny, nx) not in distances or new_dist < distances[(ny, nx)]:
                    distances[(ny, nx)] = new_dist
                    heapq.heappush(pq, (new_dist, ny, nx))

original_path_length = find_shortest_path()
result = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == '#':
            grid[y][x] = '.'
            if original_path_length - find_shortest_path() >= 100:
                result += 1
            grid[y][x] = '#'

print(f"result: {result}")
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')