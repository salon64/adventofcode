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

def find_shortest_path(start, end) -> int:
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

def find_dists(start, end) -> dict:
    pq = [(0, start[0], start[1])]  # (distance, y, x)
    distances = {start: 0}

    while pq:
        current_dist, y, x = heapq.heappop(pq)

        if (y, x) == end:
            return distances

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] != '#':
                new_dist = current_dist + 1
                if (ny, nx) not in distances or new_dist < distances[(ny, nx)]:
                    distances[(ny, nx)] = new_dist
                    heapq.heappush(pq, (new_dist, ny, nx))

ste_length = find_shortest_path(start, end)
ste = find_dists(start, end)
ets = find_dists(end, start)
result1 = 0
for y1, x1 in ste.keys():
    for y2, x2 in ets.keys():
        if abs(y1-y2) + abs(x1-x2) <= 20:
            # if dist at (y1, x1) + (y2. x2) + dist between them <= optimal_l - 100   aka save at least 100
            if ste_length  - (ste[y1, x1] + ets[y2, x2] + abs(y1-y2) + abs(x1-x2)) >= 100:
                result1 += 1

print(result1)
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')