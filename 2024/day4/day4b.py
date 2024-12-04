with open('2024/day4/day_4_input.txt', 'r') as file: # 2024/day4/day_4_input.txt
	data = file.read().splitlines()

data = ['....' + line + '....' for line in data]
x = len(data[0])
data = [x*"."] + [x*"."] + [x*"."] + [x*"."] + data + [x*"."] + [x*"."] + [x*"."] + [x*"."]

result = 0
for i, line in enumerate(data):
	for j, char in enumerate(line):
		left = False
		right = False
		if char != ".":
			#		M            A            S
			if data[i-1][j-1] + char + data[i+1][j+1] in ["MAS", "SAM"]: # top left to buttom right
				right = True
			
			if data[i+1][j-1] + char + data[i-1][j+1] in ["MAS", "SAM"]: # buttom left to top right
				left = True

		if left and right:
			result += 1
		
print(result)

		


