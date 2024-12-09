with open('2024/day2/day_2_input.txt', 'r') as file: # 2024/day2/day_2_input.txt 2024/day2/test
	data = file.read().splitlines()

l = []
for item in data:
	l.append(list(map(int, item.split())))

res = 0
for item in l:
	internalRes = 0
	for i in range(len(item)):
		removedList = item[:]
		removedList.pop(i)
		internalRes += all(i < j and abs(i-j) < 4 for i, j in zip(removedList, removedList[1:]))
		internalRes += all(i > j and abs(i-j) < 4 for i, j in zip(removedList, removedList[1:]))
	if internalRes > 0:
		res += 1

print(res)