from collections import defaultdict
import itertools
import re
import time
import heapq
start_time = time.time()
with open('fulldata', 'r') as file: # day_18_input.txt
    data = file.read().strip().splitlines()

available = []
want = []
av = True
for line in data:
    if av:
        available =line.split(", ")
        av = False
    else:
        if line == '':
            continue
        want.append(line)
    
cache = {}
def seal(s) -> int:
    if s not in cache:
        if len(s) == 0:
            return 1
        else:
            result = 0
            for pos in available:
                if s.startswith(pos):
                    result += seal(s[len(pos):])
            cache[s] = result
    
    return cache[s]


## p1
# res = 0
# for _, char in enumerate(want):
#     tmp = seal(char)
#     # print(f"char: {char}: {tmp}")
#     if tmp > 0:
#         res += 1

# p2
res = 0
for _, char in enumerate(want):
    res += seal(char)

print()
print(f"result: {res}")
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
