import functools
with open('2025/day7/day_7_input.txt', 'r') as file:
    data = file.read().strip()

lines = [list(line) for line in data.split('\n')]

for y, l in enumerate(lines):
    for x, char in enumerate(l):
        if char == 'S':
            start = (y,x)

@functools.cache
def go_down(pos) -> int:
    y, x = pos
    if y + 1 >= len(lines) or x < 0 or x >= len(lines[0]):
        return 0
    if lines[y][x] == '.' or lines[y][x] == 'S':
        # lines[y][x] = '|'
        return 0 + go_down((y+1, x))
    elif lines[y][x] == '^':
        return 1 + go_down((y, x-1)) + go_down((y, x+1))
    elif lines[y][x] == '|':
        return 0
total = go_down(start)
print(total+1)