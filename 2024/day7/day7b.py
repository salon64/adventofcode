import itertools

with open('2024/day7/day_7_input.txt', 'r') as file: # 2024/day7/day_7_input.txt
	data = file.read().splitlines()

numOrder = []
for line in data:
	tmp = line.split()
	tempLine = []
	for i, num in enumerate(tmp):
		if i == 0:
			tempLine.append(int(num[:len(num)-1]))
		else:
			tempLine.append(int(num))
	numOrder.append(tempLine)
	# print(tempLine)

ans = 0
for line in numOrder:
	check = line.pop(0)
	okay = False
	for ops in itertools.product(*[("*", "+", "||") for _ in range(len(line)-1)]):
		res = line[0]
		for i in range(1, len(line)):
			op = ops[i-1]
			if op == "+":
				res += line[i]
			elif op == "*":
				res *= line[i]
			elif op == "||":
				res = int(str(res)+str(line[i]))
	
		if res == check:
			okay = True
			break
	ans += check * okay
	
print(ans)


