with open('2024/day6/day_6_input.txt', 'r') as file: # 2024/day6/day_6_input.txt
	data_s = file.read().splitlines()

data_s = ['O' + line + 'O' for line in data_s]
x = len(data_s[0])
data_s = [x*"O"] + data_s + [x*"O"]

data = []
for line in data_s:
	data.append(list(line))
	
# print(data)


pos = [0, 0]
for y, line in enumerate(data):
	for x, char in enumerate(line):
		if char == "^":
			pos = [y, x]
			# print(f"{pos}")
			break
dir = 0
sum = 0
# dir: 
# 0 = up
# 1 = right
# 2 = down
# 3 = left
def update(sum):
	# print(f"{pos}")
	y = pos[0]
	x = pos[1]
	if data[y][x] != 'X':
		sum += 1
		data[y][x] = 'X'

	# for line in data:
	# 	print(line)
	# print()
	return sum

def turnRight(dir):
	return (dir+1)

loop = True
while loop:
	y = pos[0]
	x = pos[1]
	if (dir%4) == 0: # up
		if data[y-1][x] == 'O': # above y == O
			sum = update(sum)
			loop = False
			continue
		elif data[y-1][x] == '#':
			# print("go right")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum)
			pos[0] = pos[0]-1
			continue
	
	elif (dir%4) == 1: # right 
		if data[y][x+1]== 'O':
			sum = update(sum)
			loop = False
			continue
		elif data[y][x+1] == '#':
			# print("go down")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum)
			pos[1] = pos[1]+1
			continue

	elif (dir%4) == 2: # down
		if data[y+1][x] == 'O':
			sum = update(sum)
			loop = False
			continue
		elif data[y+1][x] == '#':
			# print("go left")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum)
			pos[0] = pos[0]+1
			continue
	
	elif (dir%4) == 3: # left
		if data[y][x-1] == 'O':
			# print("hit")
			sum = update(sum)
			loop = False
			continue
		elif data[y][x-1] == '#':
			# print("go up")
			dir = turnRight(dir)
			continue
		else:
			sum = update(sum)
			pos[1] = pos[1]-1
			continue 

print(sum)