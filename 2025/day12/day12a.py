import re
with open('2025/day12/day_12_input.txt', 'r') as file:
    raw = file.read().splitlines()

shapes = []
current = []
placements = []

mode = "shapes"  # start in shapes section
for line in raw:
    line = line.strip()
    if not line:
        continue

    if re.fullmatch(r'\d+\s*:', line):
        if current:
            shapes.append(current)
            current = []
        continue

    if ':' in line:
        left, right = map(str.strip, line.split(':', 1))
        if 'x' in left or re.fullmatch(r'[\d\s]+', right):
            mode = "placements"

    if mode == "shapes":
        if all(c in '.#' for c in line):
            current.append(line)
        else:
            continue
    else:  # placements
        if ':' not in line:
            continue
        dims, nums = map(str.strip, line.split(':', 1))
        m = re.fullmatch(r'(\d+)\s*x\s*(\d+)', dims)
        if not m:
            continue
        w, h = int(m.group(1)), int(m.group(2))
        counts = [int(x) for x in nums.split() if x.isdigit()]
        placements.append((w, h, counts))
if current:
    shapes.append(current)

shape_areas = [sum(row.count('#') for row in s) for s in shapes]

def solve(grid_size: int, locations: list[int], shape_areas: list[int]):
    total = 0
    for i in range(len(locations)):
        total += locations[i] * shape_areas[i]
    return grid_size >= total

total = 0
for x, y, locations in placements:
    if solve(x*y, locations, shape_areas):
       total += 1
print(total)