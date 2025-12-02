import re
with open('2025/day2/day_2_input.txt', 'r') as file:
    data = file.read().strip()

ranges = [[int(r[0]), int(r[1])] for r in [line.split('-') for line in data.split(',')]]

invalid_ids_count = 0
for r in ranges:
    for i in range(r[0], r[1]+1):
        i = str(i)
        if bool(re.fullmatch(r"(.+)\1+", i)):
            invalid_ids_count += int(i)

print(invalid_ids_count)

# print(sum(int(i) for a,b in (map(int,r.split('-')) for r in data.split(',')) for i in map(str,range(a,b+1)) if re.fullmatch(r"(.+)\1+",i)))


