import time
start_time = time.time()
with open('2024/day10/day_10_input.txt', 'r') as file: # 2024/day10/day_10_input.txt
    data = file.read().splitlines()

lines = []
for line in data:
    l = [int(char) for char in line]
    lines.append(l[:])

visited_path = []
def hike(y, x): 
    visited_path.append((y,x))
    val = lines[y][x]
    if val == 9:
        return 1
    
    up = y != 0                  and lines[y-1][x] == val + 1  and (y-1, x) not in visited_path
    down = y != len(lines)-1     and lines[y+1][x] == val + 1  and (y+1, x) not in visited_path
    right = x != len(lines[0])-1 and lines[y][x+1] == val + 1  and (y, x+1) not in visited_path
    left = x != 0                and lines[y][x-1] == val + 1  and (y, x-1) not in visited_path
    up_res = 0
    donw_res = 0
    right_res = 0
    left_res = 0

    if up:      
        up_res = hike(y-1, x)

    if down:
        donw_res = hike(y+1, x)

    if right:
        right_res = hike(y, x+1)

    if left:
        left_res = hike(y, x-1)
    
    return up_res + donw_res + right_res + left_res

total_res = 0
count = 0
# go over all nodes, if == 0 call a functin and begin a hike
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 0:
            visited_path = []

            s = hike(y, x)
            total_res += s
            count += 1

            # print(f"{count}: {s}")

print(total_res)
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
