with open('2024/day4/day_4_input.txt', 'r') as file: # 2024/day4/day_4_input.txt
	data = file.read().splitlines()

data = ['....' + line + '....' for line in data]
x = len(data[0])
data = [x*"."] + [x*"."] + [x*"."] + [x*"."] + data + [x*"."] + [x*"."] + [x*"."] + [x*"."]

result = 0
for i, line in enumerate(data):
	for j, char in enumerate(line):
		if char != ".":
			if "".join(line[j:j+4]) in ["XMAS", "SAMX"]: # lef to right 
				result += 1
			
			if char + data[i+1][j] + data[i+2][j] + data[i+3][j] in ["XMAS", "SAMX"]: # top to down
				result += 1
			
			if char + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3] in ["XMAS", "SAMX"]: #diagonal left
				result += 1

			if char + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3] in ["XMAS", "SAMX"]: #diagonal right
				result += 1
			
print(result)

		


