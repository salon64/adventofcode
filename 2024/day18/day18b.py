import re
import time
import heapq
start_time = time.time()
with open('2024/day18/day_18_input.txt', 'r') as file: # day_18_input.txt
    data = file.read().strip().splitlines()

grid = []
max_l = 71
for i in range(0,max_l):
    grid.append(list(max_l*"."))
blocks = []
for line in data:
    blocks.append([int(s) for s in re.findall(r'\b\d+\b', line)])

start = (0, 0)
end = (max_l - 1, max_l - 1)
rows, cols = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

for xb, yb in blocks:
    grid[yb][xb] = '#'
    shortest_path = float('inf')
    pq = [(0, start[0], start[1])]
    distances = {(start[0], start[1]): 0}
    while pq:
        current_dist, x, y = heapq.heappop(pq)
        if (x, y) == end:
            shortest_path = current_dist
            break 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.':  # Valid and not blocked
                new_dist = current_dist + 1
                if (nx, ny) not in distances or new_dist < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

    if shortest_path == float('inf'):
        print(f"{xb},{yb}")
        break

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')