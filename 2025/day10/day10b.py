from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, value, PULP_CBC_CMD
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
    for j, char in enumerate(line):
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
            if line[j-1].isdigit():
                tmp.append(int(str(tmp.pop(-1)) + char))
            else: 
                tmp.append(int(char))
        elif char == '.':
            tmp.append(0)
        elif char == '#':
            tmp.append(1)
        else: 
            continue
    operations.append(t.copy())


def solve(operations, target):
    n_ops = len(operations)
    n_bits = len(target)

    prob = LpProblem("MinButtonPresses", LpMinimize)

    # variables = number of times to press each operation
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(n_ops)]

    prob += lpSum(x)

    for j in range(n_bits):
        prob += lpSum(operations[i][j]*x[i] for i in range(n_ops)) == target[j]

    prob.solve(PULP_CBC_CMD(msg=False))

    solution = [int(value(var)) for var in x]
    total_presses = sum(solution)

    return total_presses


# target = [3,5,4,7]
# operations = [
#     [0,0,0,1],
#     [0,1,0,1],
#     [0,0,1,0],
#     [0,0,1,1],
#     [1,0,1,0],
#     [1,1,0,0]
# ]

total = 0
for i in range(len(voltages)):
    o = operations[i]
    v = voltages[i]
    total += solve(o, v)
print(total)