import time
from collections import defaultdict

start_time = time.time()
with open('2024/day11/test', 'r') as file: # 2024/day11/day_11_input.txt
    data = file.read().split(" ")

print(data)
values = defaultdict(list)

def blink(char, blinks):
    if blinks == 0:
        return 1
    
    inner_res = 0
    if char == '0':
        mod_char = "1"
        return blink(mod_char, blinks-1)

    if len(char)%2 == 0:
        l, r = char[:len(char)//2], char[len(char)//2:]
        l, r = str(int(l)), str(int(r))
        return blink(l, blinks-1) + blink(r, blinks-1)

    else:
        mod_char = str(int(char)*2024)
        return blink(mod_char, blinks-1)
    
res = 0
for val in data:
    res += blink(val, 25)
    # print("-")

print(res)
print("done")
    












end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
