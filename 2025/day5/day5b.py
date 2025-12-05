with open('2025/day5/day_5_input.txt', 'r') as file:
    data = file.read().strip()

ranges = []
for line in data.splitlines():
    if '-' in line and line != '':
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

sorted_ranges = sorted(ranges, key=lambda x: x[0])

merged_ranges = []
start, end = sorted_ranges[0]
for i, r in enumerate(sorted_ranges[1:]):
    n_start, n_end = r
    if n_end < end:
        continue
    if n_start <= end:
        end = n_end
    else:
        merged_ranges.append((start,end))
        start, end = n_start, n_end
    if i == len(sorted_ranges) - 2:
        merged_ranges.append((start, end))

total = 0
for r in merged_ranges:
    start, end = r
    total += end - start + 1
print(total)