import copy

with open('2024/day6/day_6_input.txt', 'r') as file: # 2024/day6/day_6_input.txt
	data_s = file.read().splitlines()

data_s = ['O' + line + 'O' for line in data_s]
x = len(data_s[0])
data_s = [x*"O"] + data_s + [x*"O"]


data = []
for line in data_s:
	data.append(list(line))
data_c = copy.deepcopy(data)

pos = [0, 0]
startPos = [0, 0]
for y, line in enumerate(data):
	for x, char in enumerate(line):
		if char == "^":
			pos = [y, x]
			startPos = [y, x]
			break
dir = 0
sum = 0
obstructions = 0

def update(sum, dir):
	y = pos[0]
	x = pos[1]
	if data[y][x] == '.':
		if (dir%4) == 0:
			data[y][x] = '^'
		elif (dir%4) == 1:
			data[y][x] = '>'
		elif (dir%4) == 2:
			data[y][x] = 'v'
		elif (dir%4) == 3:
			data[y][x] = '<'

	return sum

def turnRight(dir):
	y = pos[0]
	x = pos[1]
	data[y][x] = '+'
	return (dir+1)%4

placesVisited = []
loop = True
while loop:
	y = pos[0]
	x = pos[1]
	if pos not in placesVisited:
		placesVisited.append(pos[:])
		# print(f"hit {placesVisited}")

	if (dir%4) == 0: # up
		if data[y-1][x] == 'O': # above y == O
			sum = update(sum, dir)
			loop = False
			continue
		elif data[y-1][x] == '#':
			# print("go right")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum, dir)
			pos[0] = pos[0]-1
			continue
	
	elif (dir%4) == 1: # right 
		if data[y][x+1]== 'O':
			sum = update(sum, dir)
			loop = False
			continue
		elif data[y][x+1] == '#':
			# print("go down")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum, dir)
			pos[1] = pos[1]+1
			continue

	elif (dir%4) == 2: # down
		if data[y+1][x] == 'O':
			sum = update(sum, dir)
			loop = False
			continue
		elif data[y+1][x] == '#':
			# print("go left")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum, dir)
			pos[0] = pos[0]+1
			continue
	
	elif (dir%4) == 3: # left
		if data[y][x-1] == 'O':
			sum = update(sum, dir)
			loop = False
			continue
		elif data[y][x-1] == '#':
			# print("go up")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum, dir)
			pos[1] = pos[1]-1
			continue 

def updateSak(sum, posc, datac):
	y = posc[0]
	x = posc[1]

	if datac[y][x] in ['.','^']:
		datac[y][x] = '1'
		return (1, datac)

	if datac[y][x]  == '1':
		datac[y][x] = '2'
		return (2, datac)
	
	if datac[y][x] == '2':
		datac[y][x] = '3'
		return (3, datac)
	
	if datac[y][x] == '3':
		datac[y][x] = '4'
		return (4, datac)
	
	if datac[y][x] == '4':
		return (5, datac)

	return (-1, [])

def turnRight2(dir):
	return (dir+1)%4


for i, place in enumerate(placesVisited):
	if place == placesVisited[0]:
		continue
	dataWithObstacle = copy.deepcopy(data_c)
	a = place[0]
	b = place[1]
	dataWithObstacle[a][b] = '#'

	pos = startPos[:]
	dir = 0
	sum = 0
	loop = True
	while loop:
		y = pos[0]
		x = pos[1]

		if (dir%4) == 0: # up
			if dataWithObstacle[y-1][x] == 'O': 
				loop = False
				continue
			elif dataWithObstacle[y-1][x] == '#':
				dir = turnRight2(dir)
				continue
			else:
				sum, dataWithObstacle = updateSak(dir, pos, dataWithObstacle)
				pos[0] = pos[0]-1
		
		elif (dir%4) == 1: # right 
			if dataWithObstacle[y][x+1]== 'O':
				loop = False
				continue
			elif dataWithObstacle[y][x+1] == '#':
				dir = turnRight2(dir)
				continue
			else:
				res = updateSak(dir, pos, dataWithObstacle)
				sum, dataWithObstacle = res
				pos[1] = pos[1]+1

		elif (dir%4) == 2: # down
			if dataWithObstacle[y+1][x] == 'O':
				loop = False
				continue
			elif dataWithObstacle[y+1][x] == '#':
				dir = turnRight2(dir)
				continue
			else:
				sum, dataWithObstacle = updateSak(dir, pos, dataWithObstacle)
				pos[0] = pos[0]+1
		
		elif (dir%4) == 3: # left
			if dataWithObstacle[y][x-1] == 'O':
				loop = False
				continue
			elif dataWithObstacle[y][x-1] == '#':
				dir = turnRight2(dir)
				continue
			else:
				sum, dataWithObstacle = updateSak(dir, pos, dataWithObstacle)
				pos[1] = pos[1]-1

		if sum == 5:
			obstructions += 1
			break



print("done for real")
print(obstructions)
# 1935