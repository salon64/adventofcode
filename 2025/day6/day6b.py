with open('2025/day6/day_6_input.txt', 'r') as file:
    data = file.read().splitlines()

operators = []

col = [list(item) for item in zip(*data[:4])]
operators = [item for item in data[4].split()]

op_index = 0
total = 0
inner_total = 1 if operators[0] == '*' else 0
for c in col:
    if c == [' ', ' ', ' ', ' ']:
        op_index += 1
        total += inner_total
        inner_total = 1 if operators[op_index] == '*' else 0
    else:
        num = int(''.join(c))
        if operators[op_index] == '*':
            inner_total *= num
        elif operators[op_index] == '+':
            inner_total += num
total += inner_total
print(total)