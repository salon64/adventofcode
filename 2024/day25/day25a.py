import time
import copy
import networkx as nx
from functools import cache
start_time = time.time()
with open('2024/day25/day_25_input.txt', 'r') as file: # day_25_input.txt
    data = file.read().strip().splitlines()

data = [list(line) for line in data]
locks = []
keys = []

i = 0
# print(data[i])
# print(data[i+8])
# print(data[i+16])
while i < len(data):
    # print(data[i])
    if data[i] == list('#####'):
        locks.append(copy.deepcopy(data[i:i+7]))
        i+=8
        continue
    elif data[i] == list('.....'):
        keys.append(copy.deepcopy(data[i:i+7]))
        i+=8
        continue

lock_heights = []
for lock in locks:
    a = b = c = d = f = -1
    # print(lock)
    for q, w, e, r, t in lock:
        if q == '#':
            a+=1
        if w == '#':
            b+=1
        if e == '#':
            c+=1
        if r == '#':
            d+=1
        if t == '#':
            f+=1
    lock_heights.append([a,b,c,d,f])

key_heights = []
for key in keys:
    a = b = c = d = f = -1
    for q, w, e, r, t in key:
        if q == '#':
            a+=1
        if w == '#':
            b+=1
        if e == '#':
            c+=1
        if r == '#':
            d+=1
        if t == '#':
            f+=1
    key_heights.append([a,b,c,d,f])


# for lock_height in lock_heights:
#     print(lock_height)
# for key_height in key_heights:
#     print(key_height)
        
result = 0
for key_height in key_heights:
    for lock_height in lock_heights:
        okay = True
        if key_height[0] + lock_height[0] > 5:
            okay = False
        if key_height[1] + lock_height[1] > 5:
            okay = False
        if key_height[2] + lock_height[2] > 5:
            okay = False
        if key_height[3] + lock_height[3] > 5:
            okay = False
        if key_height[4] + lock_height[4] > 5:
            okay = False
        # print(f"{key_height} -> {lock_height} is {okay}")
        if okay:
            result+=1
print(result)




end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')