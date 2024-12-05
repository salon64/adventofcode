with open('2024/day5/day_5_input.txt', 'r') as file: # 2024/day5/day_5_input.txt
	data = file.read().splitlines()

rules = []
updates = []
for i, item in enumerate(data):
	if item == '':
		rules = data[:i]
		updates = data[i+1:]

rules = [instr.split('|') for instr in rules]
for i, rule in enumerate(rules):
	rules[i] = [int(rule[0]), int(rule[-1])]

rules_d = {}
custom_rules = {}
for first, second in rules:
    if first not in rules_d:
        rules_d[first] = []
    rules_d[first].append(second)

updates = [[int(item) for item in update.split(',')] for update in updates]

def lawAbidingNumber(num1, num2):
	return num1 in rules_d and num2 in rules_d[num1]

def sortingTheNumbersInAWayThatWillNotCauseMeShame(update):
	sortedList = []
	for item in update:
		pos = len(update)-1
		for i, sortedItem in enumerate(sortedList):
			if lawAbidingNumber(sortedItem, item):
				pos = i
				break
		sortedList.insert(pos, item)
	return sortedList

# wow
result = 0
for i, update in enumerate(updates):
	okay = True
	for j, item in enumerate(update):
		if item in rules_d:
			for val in rules_d[item]:
				while val in update[:j]:
					okay = False
					break

	if not okay:
		update = sortingTheNumbersInAWayThatWillNotCauseMeShame(update)
		result += update[int(len(update)/2)]


print(result)
# 4971



# def fix(update):
# 	for j, item in enumerate(update):
# 		if item in rules_d:
# 			for val in rules_d[item]:
# 				if val in update[:j]:
# 					swapPos = 0
# 					for s, ite in enumerate(update):
# 						if val == ite:
# 							swapPos = s

# 					update[j], update[swapPos] = update[swapPos], update[j]
# 					# print(update)
# 					fix(update)
	
# 	return(update)
		
