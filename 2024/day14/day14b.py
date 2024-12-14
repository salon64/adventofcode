from collections import defaultdict
import time
import re
import os
from PIL import Image, ImageDraw
start_time = time.time()
with open('2024/day14/day_14_input.txt', 'r') as file: # day_14_input.txt
    data = file.read().strip().splitlines()

drones = [] # x y xV yV
for line in data:
    drones.append([int(s) for s in re.findall(r'-?\b\d+\b', line)])

width = 101
height = 103
tl = tr = bl = br = 0
new_loc = defaultdict(int)

output_folder = "2024/day14/drone_tiles"
os.makedirs(output_folder, exist_ok=True)
def generate_image(new_loc, step):
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    for y in range(height):
        for x in range(width):
            if (x, y) in new_loc:
                draw.point((x, y), fill='black')  # Mark as #

    image.save(os.path.join(output_folder, f'step_{step:04d}.png'))

for i in range(6752,6753):
    new_loc.clear()
    for drone in drones:
        new_x = (drone[0]+drone[2]*i) % width
        new_y = (drone[1]+drone[3]*i) % height
        new_loc[(new_x, new_y)] += 1
    generate_image(new_loc, i)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
