with open('2025/day3/day_3_input.txt', 'r') as file:
    data = file.read().strip()

lines = data.split('\n')
sum = 0

for line in lines:
    # print(line)
    max_left = 0
    max_right = 0
    for i, char in enumerate(line):
        # print(char)
        num = int(char)
        if num > max_left and i != len(line)-1:
            max_left = num
            max_right = 0
        elif num >= max_right:
            max_right = num

        # print(f"max_left:{max_left}, max_right={max_right}")
    # print(f"max_left:{max_left}, max_right={max_right}")
    sum += int(str(max_left)+str(max_right))

print(sum)
            
