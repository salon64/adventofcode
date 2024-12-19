import time
start_time = time.time()
with open('2024/day19/day_19_input.txt', 'r') as file: 
    data = file.read().strip().splitlines()

available = []
want = []
av = True
for line in data:
    if av:
        available =line.split(", ")
        av = False
    else:
        if line == '':
            continue
        want.append(line)
    
cache = {}
def seal(s) -> int:
    if s not in cache:
        if len(s) == 0:
            return 1
        else:
            result = 0
            for pos in available:
                if s.startswith(pos):
                    result += seal(s[len(pos):])
            cache[s] = result
    return cache[s]

res = 0
for _, char in enumerate(want):
    res += seal(char)

print(f"result: {res}")
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
