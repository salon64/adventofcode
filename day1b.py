input = []
left = []
right = []


with open('day1data') as f:
    input = f.read().strip().split()
    for i, data in enumerate(input):
        # print(f"i: {i}, data: {data}")
        if i % 2 == 0:
            left.append(int(data))
        else:
            right.append(int(data))

leftDict = {}


for i in range(len(left)): 
    leftDict[left[i]] = 0

for item in right:
    if item in leftDict:
        leftDict[item] = leftDict.get(item) + 1

result = 0
for item in left:
    if item in leftDict:
        result += item * leftDict.get(item)

print(result)