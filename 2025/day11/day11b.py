import functools
with open('2025/day11/day_11_input.txt', 'r') as file:
    data = file.read().strip()

routes = {}

for line in data.splitlines():
    line = line.strip()
    if not line:
        continue

    src, rhs = line.split(":", 1)
    src = src.strip()
    targets = [t.strip() for t in rhs.split() if t]

    routes[src] = targets 
    
@functools.cache
def count_paths(curr, end):
    if curr == end:
        return 1
    if curr not in routes:
        return 0 

    total = 0
    for nxt in routes[curr]:
        total += count_paths(nxt, end)
    return total
    
p1 = count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
p2 = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")

print(p1 + p2)