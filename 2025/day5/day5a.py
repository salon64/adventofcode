with open('2025/day5/day_5_input.txt', 'r') as file:
    data = file.read().strip()

ranges = []
IDs = []
for line in data.splitlines():
    if '-' in line and line != '':
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    elif line != '':
        IDs.append(int(line))

total = 0
for id in IDs:
    for start, end in ranges:
        if start <= id <= end:
            total += 1
            break

print(total)