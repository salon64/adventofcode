with open('2025/day4/day_4_input.txt', 'r') as file:
    data = file.read().strip().splitlines()
grid = [list(row) for row in data]

dirs = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1))
total = 0
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
        
        print(f"At ({y},{x}), locations hit: {locations_hit}")
        if count < 4:
            total += 1

# for row in grid:
#     print(''.join(row))

print(total)
            