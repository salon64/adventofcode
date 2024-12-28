from collections import defaultdict
import time
import heapq
start_time = time.time()
with open('2024/day16/day_16_input.txt', 'r') as file: # day_16_input.txt
    data = file.read().strip().splitlines()
grid = [list(row) for row in data]
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'S':
            sy,sx = y, x
        elif char == 'E':
            ey,ex = y, x

sd = 0
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
def adjs(cur):
    cy, cx, cd  = cur
    yield 1000, (cy, cx, (cd-1)%4)
    yield 1000, (cy, cx, (cd+1)%4)
    dy, dx = dirs[cd]
    ny, nx = cy+dy, cx+dx
    if grid[ny][nx] != '#':
        yield 1, (ny, nx, cd)

start = (sy, sx, sd)
pq = []
p1 = None
heapq.heappush(pq, (0, start))
dists = defaultdict(lambda : float("inf"))
from_ = defaultdict(lambda : set())
while pq:
    dist, cur = heapq.heappop(pq)
    (cy, cx, cd) = cur

    for d, adj in adjs(cur):
        if d + dist < dists[adj]:
            dists[adj] = d + dist
            heapq.heappush(pq, (dists[adj], adj))
            from_[adj] = {cur}
        elif d + dist == dists[adj]:
            from_[adj].add(cur)

stack = [(ey, ex, 1)]
gnodes = set(stack)
while stack:
    some = stack.pop(-1)
    for other in from_[some]:
        if other not in gnodes:
            gnodes.add(other)
            stack.append(other)

gnodes = set(x[:2] for x in gnodes)
print(len(gnodes))
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')














# shortest_path_length = float('inf')
# paths = []
# def dfs(y, x, dir, distance, path):
#     global shortest_path_length
#     path.append((y, x))
#     if len(path) > 1000:
#         return
#     if distance > shortest_path_length:
#         return
#     if data[y][x] == 'E':
#         shortest_path_length = min(shortest_path_length, distance)
#         paths.append((distance, path[:]))
#     for dy, dx, new_dir in [(-1, 0, 0), (1, 0, 2), (0, 1, 1), (0, -1, 3)]:  # (dy, dx, direction)
#         ny, nx = y + dy, x + dx
#         if data[ny][nx] == '#' or (ny, nx) in path:
#             continue
#         turn_penalty = 1000 if new_dir != dir else 0
#         new_dist = distance + 1 + turn_penalty
#         dfs(ny, nx, new_dir, new_dist, path[:])

# dfs(start_pos[0], start_pos[1], 1, 0, []) # y, x, dir, distance, path

# res = set()
# for distance, path in paths:
#     # print(distance)
#     if distance == shortest_path_length:
#         for node in path:
#             res.add(node)

# print(len(res))
# print(f"shortest path: {shortest_path_length}")
# end_time = time.time()
# print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')


# for y, x in res:
#     data[y][x] = 'O'
# for line in data:
#     print("".join(line))

# def is_valid(y, x, dir, new_dist, oy, ox):
#     if (y, x) in distances:
#         existing_dist, old_dir = distances[(y, x)]
#         if abs(existing_dist - new_dist) == 1000: # and (y, x) != end_pos and dir != old_dir
#             source_nodes[(y, x)].append((oy, ox))
#             return False
#         elif existing_dist < new_dist:
#             return False
#         elif existing_dist > new_dist:
#             source_nodes[(y, x)] = [(oy, ox)]
#     else:
#         distances[(y, x)] = (new_dist, dir)
#         source_nodes[(y, x)] = [(oy, ox)]
#     return data[y][x] != '#'  # Not a wall

# q = queue()
# q.append((pos[0], pos[1], 1, 0))  # (y, x, direction, distance)
# distances[(pos[0], pos[1])] = (0, 1)
# shortest_path_length = float('inf')
# while (len(q) > 0):
#     y, x, dir, dist = q.popleft()
#     if data[y][x] == 'E':
#         shortest_path_length = min(shortest_path_length, dist)
#         continue

#     for dy, dx, new_dir in [(-1, 0, 0), (1, 0, 2), (0, 1, 1), (0, -1, 3)]:  # (dy, dx, direction)
#         ny, nx = y + dy, x + dx
#         turn_penalty = min(abs(dir - new_dir), 4 - abs(dir - new_dir)) * 1000
#         new_dist = dist + 1 + turn_penalty

#         if is_valid(ny, nx, dir, new_dist, y, x):
#             distances[(ny, nx)] = (new_dist, dir)
#             q.append((ny, nx, new_dir, new_dist))

# res = set()
# res.add(end_pos)
# q2 = queue()
# q2.append(end_pos)
# while q2:
#     origin = q2.popleft()
#     if origin == pos:
#         res.add(origin)  # Always add the start position once it's reached
#     for source in source_nodes[origin]:
#         if source not in res:  # Avoid adding already processed nodes
#             res.add(source)
#             q2.append(source)

# for y, x in res:
#     data[y][x] = 'O'
# for line in data:
#     print("".join(line))

# print(distances)