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
            fences[-1].add((y-0.1, x, '-'))
    if not down:
            fences[-1].add((y+0.1, x, '-'))
    if not right:
            fences[-1].add((y, x+0.1, '|'))
    if not left:
            fences[-1].add((y, x-0.1, '|'))

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
            fences.append(set())
            nextNode(y, x)

sides = []
res = 0
for ind, fence_set in enumerate(fences):
    fence_set = list(fence_set)
    x_breaks = 1
    y_breaks = 1

    fence_set.sort(key=lambda x: (x[0], x[1])) # sort on y
    for i in range(1, len(fence_set)):
        if fence_set[i][2] == '|':
            continue
        if fence_set[i-1][1]+1 != fence_set[i][1] or fence_set[i-1][2] == '|':
            x_breaks+=1 
            continue
        elif fence_set[i-1][0] != fence_set[i][0]:
            x_breaks+=1
            continue 
    
    fence_set.sort(key=lambda x: (x[1], x[0])) # sort on x
    for i in range(1, len(fence_set)):
        if fence_set[i][2] == '-':
            continue
        if fence_set[i-1][0]+1 != fence_set[i][0] or fence_set[i-1][2] == '-':
            y_breaks+=1 
            continue
        elif fence_set[i-1][1] != fence_set[i][1]:
            y_breaks+=1
            continue 
    res += (x_breaks+y_breaks)*regions[ind]
print(res)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
