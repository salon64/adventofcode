from collections import defaultdict
import time
import re
start_time = time.time()
with open('2024/day14/day_14_input.txt', 'r') as file: # day_14_input.txt
    data = file.read().strip().splitlines()

drones = [] # x y xV yV
for line in data:
    drones.append([int(s) for s in re.findall(r'-?\b\d+\b', line)])

width = 101
height = 103
tl = tr = bl = br = 0
new_loc = defaultdict(int)
for i in range(0,10000):
    for drone in drones:
        new_x = (drone[0]+drone[2]*100) % width
        new_y = (drone[1]+drone[3]*100) % height
        new_loc[(new_x, new_y)] += 1

        # slit em up
        left = True if new_x < (width//2) else False
        right = True if new_x > (width//2) else False
        top = True if new_y < (height//2) else False
        down = True if new_y > (height//2) else False
        if top and left:
            tl += 1
        elif top and right:
            tr += 1
        elif down and left:
            bl += 1
        elif down and right:
            br += 1

print(tl * tr * bl * br)
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
