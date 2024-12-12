import time
start_time = time.time() 
with open('2024/day12/day_12_input.txt', 'r') as file: # day_12_input.txt
    data = file.read().strip().splitlines()

lines=[]
for line in data:
    lines.append(list(line))

visited_nodes = set()
regions = []
fences = []

def nextNode(y, x):
    visited_nodes.add((y, x))
    regions[-1]+=1

    up    = y != 0               and lines[y-1][x] == lines[y][x]
    down  = y != len(lines)-1    and lines[y+1][x] == lines[y][x]
    right = x != len(lines[0])-1 and lines[y][x+1] == lines[y][x]
    left  = x != 0               and lines[y][x-1] == lines[y][x]

    if not up:
            fences[-1] += 1
    if not down:
            fences[-1] += 1
    if not right:
            fences[-1] += 1
    if not left:
            fences[-1] += 1

    if up:
        if (y-1, x) not in visited_nodes:
            nextNode(y-1, x)
    if down:
        if (y+1, x) not in visited_nodes:
            nextNode(y+1, x)
    if right:
        if (y, x+1) not in visited_nodes:
            nextNode(y, x+1)
    if left:
        if (y, x-1) not in visited_nodes:
            nextNode(y, x-1)
    return

index = -1
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if (y, x) not in visited_nodes:
            regions.append(0)
            fences.append(0)
            nextNode(y, x)

res = 0
for i in range(0, len(fences)):
    res += regions[i]*fences[i]
print(res)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
