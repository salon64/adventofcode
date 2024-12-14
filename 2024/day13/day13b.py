import time
import re
import numpy as np
start_time = time.time()
with open('2024/day13/day_13_input.txt', 'r') as file: # day_13_input.txt
    data = file.read().splitlines()

A = []
B = []
P = []
results = []
i = 0
for i, line in enumerate(data):
    if line == '':
        A.append([int(s) for s in re.findall(r'\b\d+\b', data[i-3])])
        B.append([int(s) for s in re.findall(r'\b\d+\b', data[i-2])])
        P.append([int(s)+10000000000000 for s in re.findall(r'\b\d+\b', data[i-1])])

res = 0
for game in range(0, len(P)):
    a = np.array([[A[game][0], B[game][0]], [A[game][1], B[game][1]]])
    b = np.array([P[game][0], P[game][1]])
    x = np.linalg.solve(a,b).tolist()
    x = np.round(x, 3).tolist()
    if int(x[0]) == x[0] and int(x[1]) == x[1]:
        res += x[0]*3 + x[1]

print(int(res))

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
