import time
start_time = time.time()
with open('2024/day15/test', 'r') as file: # day_15_input.txt
    data = file.read().strip().splitlines()

pos = (0, 0)
gps = []
moves = ""
moves_bool = False
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == '@':
            pos = (y, x)
    if line == '':
        moves_bool = True
    elif not moves_bool:
        gps.append(list(line))
    elif moves_bool:
        moves+=line
moves = list(moves)

def push(pos, dir):
    y, x = pos
    if gps[y][x] == '.':
        return dir
    elif gps[y][x] == '#':
        return (0,0)
    elif gps[y][x] == 'O':
        new_dir = push((pos[0]+dir[0], pos[1]+dir[1]), dir)
        gps[y][x], gps[y+new_dir[0]][x+new_dir[1]] = gps[y+new_dir[0]][x+new_dir[1]], gps[y][x]
        return new_dir
    elif gps[y][x] == '@':
        new_dir = push((pos[0]+dir[0], pos[1]+dir[1]), dir)
        gps[y][x], gps[y+new_dir[0]][x+new_dir[1]] = gps[y+new_dir[0]][x+new_dir[1]], gps[y][x]
        return (y+new_dir[0], x+new_dir[1])

for move in moves:
    if move == '^':
        pos = push(pos, (-1, 0))
    if move == 'v':
        pos = push(pos, (1, 0))
    if move == '>':
        pos = push(pos, (0, 1))
    if move == '<':
        pos = push(pos, (0, -1))

res = 0
for y, line in enumerate(gps):
    for x , char in enumerate(line):
        if char == 'O':
            res += 100*y + x
print(f"{res}")
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
