with open('2025/day2/day_2_input.txt', 'r') as file:
    data = file.read().strip()

# ranges = []
# for line in data.split(','):
#     print(line)
#     r = line.split('-')
#     print(r)
#     ranges.append([r[0], r[1]])

ranges = [[int(r[0]), int(r[1])] for r in [line.split('-') for line in data.split(',')]]

invalid_ids_count = 0
for r in ranges:
    for i in range(r[0], r[1]+1):
        i = str(i)
        if len(i) % 2 != 0:
            continue
        if i[:len(i)//2] == i[len(i)//2:]:
            invalid_ids_count += int(i)

print(invalid_ids_count)