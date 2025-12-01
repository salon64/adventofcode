import time
with open('2025/day1/day_1_input.txt', 'r') as file:
    data = file.read().strip()

dial_actions = []
position = 50
counter = 0

for line in data.splitlines():
    # print(line)
    first_char = line[0]
    rest_of_line = line[1:]
    dial_actions.append((first_char, int(rest_of_line)))

for action in dial_actions:
    if action[0] == 'L':
        position = (position - action[1]) % 100
    else:
        position = (position + action[1]) % 100
    # print(position)
    if position == 0:
        counter += 1

print(counter)