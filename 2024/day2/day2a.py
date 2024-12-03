with open('2024/day2/day_2_input.txt', 'r') as file: # 2024/day2/day_2_input.txt
	data = file.read().splitlines()


l = []
for item in data:
	l.append(list(map(int, item.split())))


res = 0
for item in l:
	res += all(i < j and abs(i-j) < 4 for i, j in zip(item, item[1:]))
	res += all(i > j and abs(i-j) < 4 for i, j in zip(item, item[1:]))

print(res)