import time
import copy
start_time = time.time()
with open('2024/day15/day_15_input.txt', 'r') as file: # day_15_input.txt
    data = file.read().strip().splitlines()

pos = (0, 0)
gps = []
moves = ""
moves_bool = False
for y, line in enumerate(data):
    if line == '':
        moves_bool = True
        continue
    if not moves_bool:
        tmp = ""
        for char in line:
            if char == '#':
                tmp += "##"
            elif char == 'O':
                tmp += "[]"
            elif char == '.':
                tmp += ".."
            elif char == "@":
                tmp += "@."

        gps.append(list(tmp))
    elif moves_bool:
        moves+=line
moves = list(moves)

for y, line in enumerate(gps):
    for x, char in enumerate(line):
        if char == '@':
            pos = (y, x)
            break
        
def push(pos, dir, q):
    global okay
    y, x = pos
    yV, xV = dir
    if gps[y][x] == '.':
        return dir
    elif gps[y][x] == '#':
        okay = False
        return (0,0)
    elif gps[y][x] == '@':
        new_dir = push((y+dir[0], x+dir[1]), dir, 1)
        if okay:
            gps[y][x], gps[y+new_dir[0]][x+new_dir[1]] = gps[y+new_dir[0]][x+new_dir[1]], gps[y][x]
            return (y+new_dir[0], x+new_dir[1])
        if not okay: 
            return pos
    elif (gps[y][x] == '[' or gps[y][x] == ']') and (dir == (0, 1) or dir == (0, -1)):
        new_dir = push((y+dir[0], x+dir[1]), dir, 1)
        gps[y][x], gps[y+new_dir[0]][x+new_dir[1]] = gps[y+new_dir[0]][x+new_dir[1]], gps[y][x]
        return new_dir
    if gps[y][x] == '[' and (dir == (-1, 0) or dir == (1, 0)):
        if q == 1:
            side_dir = push((y, x+1), dir, 0)
        new_dir = push((y+yV, x+xV), dir, 1)
        gps[y][x], gps[y+new_dir[0]][x+new_dir[1]] = gps[y+new_dir[0]][x+new_dir[1]], gps[y][x]
        return new_dir
    elif gps[y][x] == ']' and (dir == (-1, 0) or dir == (1, 0)):
        if q == 1:
            side_dir = push((y, x-1), dir, 0)
        new_dir = push((y+yV, x+xV), dir, 1)
        gps[y][x], gps[y+new_dir[0]][x+new_dir[1]] = gps[y+new_dir[0]][x+new_dir[1]], gps[y][x]
        return new_dir

for move in moves:
    sasaved_state = copy.deepcopy(gps)
    okay = True
    if move == '^':
        pos = push(pos, (-1, 0), 1)
    if move == 'v':
        pos = push(pos, (1, 0), 1)
    if move == '>':
        pos = push(pos, (0, 1), 1)
    if move == '<':
        pos = push(pos, (0, -1), 1)
    if not okay:
        gps = copy.deepcopy(sasaved_state)
    
res = 0
for y, line in enumerate(gps):
    for x , char in enumerate(line):
        if char == '[':
            res += 100*y + x
print(f"{res}")
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
