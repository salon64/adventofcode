with open('2024/day8/day_8_input.txt', 'r') as file: # 2024/day8/day_8_input.txt
	data = file.read().splitlines()
import math
import time
start = time.time()

lines = []
for line in data:
	lines.append(list(line))
	
locations = []
for y, line in enumerate(lines):
	for x, char in enumerate(line):
		if char != '.':
			locations.append((char, y, x))


validNoise = set()
for i, locA in enumerate(locations):
	for j, locB in enumerate(locations):
		if locA[0] == locB[0] and i != j:
			xDist = locA[2] - locB[2] 
			yDist = locA[1] - locB[1] 

			mul = 1
			pos = True
			neg = True
			while pos == True or neg == True:
				xT = (mul * xDist)
				yT = (mul * yDist)
				x = locA[2]
				y = locA[1]

				if x + xT not in range(0, len(lines[0])) or y + yT not in range(0, len(lines)):
					pos = False
				if x - xT not in range(0, len(lines[0])) or y - yT not in range(0, len(lines)):
					neg = False
				
				if pos:
					validNoise.add((y+yT, x+xT))
				if neg:
					validNoise.add((y-yT, x-xT))

				mul+=1


print(len(validNoise))

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")