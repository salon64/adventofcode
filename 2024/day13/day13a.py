import time
import re
start_time = time.time()
with open('2024/day13/day_13_input.txt', 'r') as file: # day_13_input.txt
    data = file.read().splitlines()

# print(data)
T = list(range(100))
A = []
B = []
P = []
results = []
i = 0
for i, line in enumerate(data):
    if line == '':
        A.append([int(s) for s in re.findall(r'\b\d+\b', data[i-3])])
        B.append([int(s) for s in re.findall(r'\b\d+\b', data[i-2])])
        P.append([int(s) for s in re.findall(r'\b\d+\b', data[i-1])])

for game in range(0, len(P)):
    for i in range(0,100):
        X_matches = [] # A amount, B amount
        l = 0
        r = 100
        if A[game][0]*i > P[game][0]:
            break
        while l <= r:  # binary search
            mid = l + (r - l) // 2
            current_sum = A[game][0] * i + B[game][0] * mid

            if current_sum == P[game][0]:  # if equal
                X_matches.append([i, mid])
                break  # exit binary search loop once a match is found

            elif current_sum < P[game][0]:  # if smaller
                l = mid + 1

            else:  # if larger
                r = mid - 1

        for match in X_matches:
            if A[game][1]*match[0] + B[game][1]*match[1] == P[game][1]:
                match.append(3*match[0]+match[1])
            else:
                match.append(301)

        if X_matches:
            X_matches.sort(key=lambda x: x[2])
            if X_matches[0][2] != 301:
                results.append(X_matches[0][2])

r = 0
for res in results:
    r += res
print(r)
        
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
