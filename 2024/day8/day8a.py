with open('2024/day8/day_8_input.txt', 'r') as file: # 2024/day8/day_8_input.txt
	data = file.read().splitlines()


lines = []
for line in data:
	lines.append(list(line))
	

locations = []
for y, line in enumerate(lines):
	for x, char in enumerate(line):
		if char != '.':
			locations.append((char, y, x))

# for line in lines:
# 	print(line)

validNoise = set()
# calculate all possible locations that meet req and are in distance 50
for i, locA in enumerate(locations):
	for j, locB in enumerate(locations):
		if locA[0] == locB[0] and i != j:
			for y, line in enumerate(lines):
				for x, char in enumerate(line):
					# d1 = math.sqrt((x - locA[2])**2 + (y - locA[1])**2)
					# d2 = math.sqrt((x - locB[2])**2 + (y - locB[1])**2)
					
					# if d1.is_integer() and d2.is_integer() and (d2 == d1 * 2 or d1 == d2 * 2):
					xDist = locA[2] - locB[2] # = 1 
					yDist = locA[1] - locB[1] # = 2

					if x + xDist == locA[2] and y + yDist == locA[1]:
						if (y, x) not in [(locA[1], locA[2]), (locB[1], locB[2])]:
							validNoise.add((y, x))
						
					elif x - xDist == locA[2] and y - yDist == locA[1]:
						if (y, x) not in [(locA[1], locA[2]), (locB[1], locB[2])]:
							validNoise.add((y, x))

for y, x in validNoise:
    if lines[y][x] == '.':  
        lines[y][x] = '#'

# for line in lines:
# 	print(line)

# print(locations)
# print()
print(validNoise)
print(len(validNoise))