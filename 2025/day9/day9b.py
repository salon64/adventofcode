with open('2025/day9/day_9_input.txt', 'r') as file:
    data = file.read().strip()

points = [tuple(map(int, line.split(','))) for line in data.split('\n')]

edges = []
for i in range(len(points)):
    p1 = points[i]
    p2 = points[(i + 1) % len(points)]
    if p1[0] == p2[0]:
        x = p1[0]
        y1, y2 = sorted([p1[1], p2[1]])
        for y in range(y1 + 1, y2):
            edges.append((x, y))
    elif p1[1] == p2[1]:
        y = p1[1]
        x1, x2 = sorted([p1[0], p2[0]])
        for x in range(x1 + 1, x2):
            edges.append((x, y))

point_set = set(points)
edge_set  = set(edges)
combined_set = point_set.union(edge_set)

# for y in range(10):
#     for x in range(20):
#         if (x, y) in point_set:
#             print('#', end='')
#         elif (x, y) in edge_set:
#             print('X', end='')
#         else:
#             print('.', end='')
#     print()

def validRectangle(a, b, perimeter):
    min_x = min(a[0], b[0])
    min_y = min(a[1], b[1])
    max_x = max(a[0], b[0])
    max_y = max(a[1], b[1])

    # left
    for i in range(1, max_y - min_y):
        first = (min_x, min_y + i)
        second = (min_x + 1, min_y + i)
        if first in perimeter and second in perimeter:
            return False

    # right
    for i in range(1, max_y - min_y):
        first = (max_x, min_y + i)
        second = (max_x - 1, min_y + i)
        if first in perimeter and second in perimeter:
            return False

    # top
    for i in range(1, max_x - min_x):
        first = (min_x + i, min_y)
        second = (min_x + i, min_y + 1) 
        if first in perimeter and second in perimeter:
            return False

    # down
    for i in range(1, max_x - min_x):
        first = (min_x + i, max_y)
        second = (min_x + i, max_y - 1)
        if first in perimeter and second in perimeter:
            return False
    
    return True

largestArea = 0
perimeter = combined_set
for a in points:
    # print(f"Progress: {points.index(a) / len(points) * 100:.2f}%", end='\r')
    for b in points:
        if a == b:
            continue
        else:
            area = (abs(a[1] - b[1]) + 1) * (abs(a[0] - b[0]) + 1)
            if area > largestArea:
                if validRectangle(a, b, perimeter):
                    largestArea = area
print(largestArea)