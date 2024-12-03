with open('2024/day3/day_3_input.txt', 'r') as file: # 2024/day3/day_3_input.txt
	data = file.read()

import re

matches = list(re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data))

print(matches)
do = True
sum = 0
for i, match in enumerate(matches):
    if match[0] and match[1]:  # Groups for mul(x, y)
        if do:
         sum += int(match[0]) * int(match[1])
    elif match[2]:  # Group for do()
        do = True
    elif match[3]:  # Group for don't()
        do = False
print(sum)     

('', '', 'do()', '')