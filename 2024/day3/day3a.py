with open('2024/day3/day_3_input.txt', 'r') as file: # 2024/day3/day_3_input.txt
	data = file.read()

import re

matches = [list(match.groups()) for match in re.finditer(r"mul\((\d+),(\d+)\)", str(data))]

matchesInt = []
sum = 0
for item in matches:
	matchesInt.append(list(map(int, item)))
	sum += matchesInt[-1][0] * matchesInt[-1][1]

print(sum)
