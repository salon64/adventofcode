with open('2025/day4/day_4_input.txt', 'r') as file:
    data = file.read().strip().splitlines()
grid = [list(row) for row in data]

# print(grid)

# y, x
dirs = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1))

total_total = 0
while True:
    total = 0
    positios_to_update = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '@':
                continue
            count = 0
            locations_hit = []
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '@':
                    count += 1
                    locations_hit.append((ny, nx))
            if count < 4:
                total += 1
                positios_to_update.append((y, x))

    for y, x in positios_to_update:
        grid[y][x] = 'x'

    total_total += total
    if total == 0:
        break

print(total_total)


            