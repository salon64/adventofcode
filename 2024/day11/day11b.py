import time
import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

start_time = time.time()
with open('2024/day11/day_11_input.txt', 'r') as file: # 2024/day11/day_11_input.txt
    data = file.read().split(" ")

values = defaultdict(dict)

def blink(char, blinks_left):
    if blinks_left == 0:
        return 1
    
    if blinks_left in values[char]:
        #print(f"found: {char},  {values[char]}, bl = {blinks_left}")
        return values[char][blinks_left]

    if char == '0':
        mod_char = "1"
        inner_res = blink(mod_char, blinks_left-1)
        values[char][blinks_left] = inner_res
        return inner_res
    elif len(char)%2 == 0:
        l, r = char[:len(char)//2], char[len(char)//2:]
        l, r = str(int(l)), str(int(r))
        l_r = blink(l, blinks_left-1)
        r_r = blink(r, blinks_left-1)
        values[char][blinks_left] = l_r + r_r
        return l_r + r_r
    else:    
        mod_char = str(int(char)*2024)
        inner_res = blink(mod_char, blinks_left-1)
        values[char][blinks_left] = inner_res
        return inner_res

res = 0
dept = 500
for val in data:
    res += blink(val, dept)
    
print("done")
print(res)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
