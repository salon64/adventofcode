from itertools import combinations
with open('2025/day10/day_10_input.txt', 'r') as file:
    data = file.read().strip()

starts = []
operations = []
voltages = []

lines = [list(line) for line in data.split('\n')]
for line in lines:
    t = []
    tmp = []
    b = [0, 0 ,0]
    for char in line:
        if char == '[':
            tmp = []
        elif char == '(':
            tmp = []
        elif char == '{':
            tmp = []
        elif char == ']':
            starts.append(tmp.copy())
        elif char == ')':
            vec_len = len(starts[-1])
            vec = [0] * vec_len
            for i in tmp:
                vec[i] ^= 1
            t.append(vec.copy())
        elif char == '}':
            voltages.append(tmp.copy())
        elif char.isdigit():
            tmp.append(int(char))
        elif char == '.':
            tmp.append(0)
        elif char == '#':
            tmp.append(1)
        else: 
            continue
    operations.append(t.copy())
# print(starts)
# print(operations)
# print(voltages)


def xor_vectors(vecs):
    if not vecs:
        return None
    n = len(vecs[0])
    out = [0] * n
    for v in vecs:
        for i in range(n):
            out[i] ^= v[i]
    return out


def solve_min_xor(start_vec, operations):
    n_ops = len(operations)
    solutions = []

    for r in range(n_ops + 1):
        for combo in combinations(range(n_ops), r):
            vecs = [operations[i] for i in combo]
            if xor_vectors(vecs) == start_vec:
                solutions.append(combo)

    if not solutions:
        return 

    m = min(len(s) for s in solutions)
    # sols = [s for s in solutions if len(s) == m]
    return m


# print(starts[0])
# print(operations[0])
# result = solve_min_xor(starts[0], operations[0])
# print(result)


total = 0
for i in range(0, len(starts)):
    result = solve_min_xor(starts[i], operations[i])
    total += result
print(total)