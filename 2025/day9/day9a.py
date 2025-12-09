with open('2025/day9/day_9_input.txt', 'r') as file:
    data = file.read().strip()

points = [tuple(map(int, line.split(','))) for line in data.split('\n')]
# print(points)

area_sizes = []
for a in points:
    for b in points:
        if a == b:
            continue
        # calcualte area of rectangle
        area = abs((a[0] - b[0])+1) * (abs(a[1] - b[1]+1))
        # print(f"Area between {a} and {b}: {area}")
        area_sizes.append(area)

area_sizes = sorted(area_sizes, reverse=True)
print(area_sizes[0])