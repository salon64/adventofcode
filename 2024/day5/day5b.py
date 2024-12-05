with open('2024/day5/test', 'r') as file: # 2024/day5/day_5_input.txt
	data = file.read().splitlines()

rules = []
updates = []
for i, item in enumerate(data):
	if item == '':
		rules = data[:i]
		updates = data[i+1:]
		break

rules = [instr.split('|') for instr in rules]
for i, rule in enumerate(rules):
	rules[i] = [int(rule[0]), int(rule[-1])]

rules_d = {}
for first, second in rules:
    if first not in rules_d:
        rules_d[first] = []
    rules_d[first].append(second)

updates = [[int(item) for item in update.split(',')] for update in updates]
print(rules_d)

result = 0
for i, update in enumerate(updates):
	print(update)
	okay = True
	for j, item in enumerate(update):
		if item in rules_d:
			for val in rules_d[item]:
				while val in update[:j]:
					okay = False
					
					swapPos = 0
					for s, ite in enumerate(update):
						if val == ite:
							swapPos = s
							break
					
					update[j], update[swapPos] = update[swapPos], update[j]
					print("-----------------------------------------------------")
					print(f"false {val} in {update[:i]},   key: {item} values: {rules_d[item]}")
					print(update)
					print("--------------------------------------------------------")



	if not okay:
		# print(f"---------------- {update[int(len(update)/2)]}")
		result += update[int(len(update)/2)]

print(result)

