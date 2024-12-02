left = []
right = []


with open('2024/day1/day_1_input.txt') as f:
    input = f.read().strip().split()
    for i, data in enumerate(input):
        # print(f"i: {i}, data: {data}")
        if i % 2 == 0:
            left.append([int(data), int(i/2)])
        else:
            right.append([int(data), int((i-1)/2)])


left.sort(key=lambda x: x[0])
right.sort(key=lambda x: x[0])

# print(right)

totalDistance = 0
for i in range(len(left)): 
    
    print(f"{left[i]}  {right[i]}")
    print(abs(left[i][0] - right[i][0]))
    totalDistance += abs(left[i][0] - right[i][0])


print(totalDistance)