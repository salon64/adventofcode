with open('2025/day6/day_6_input.txt', 'r') as file:
    data = file.read().strip()

lines = []
operators = []

for line in data.splitlines():
    if '+' in line:
        operators = line.split()
    else:
        lines.append(line.split())

total_sum = 0
for i in range(len(operators)):
    op = operators[i]
    inner_sum = 0 if op == '+' else 1
    for j in range(len(lines)):
        # print(f"op: {op}, col: {lines[j][i]}")
        if op == '+':
            inner_sum += int(lines[j][i])
        elif op == '*':
            inner_sum *= int(lines[j][i])
    total_sum += inner_sum
print(total_sum)