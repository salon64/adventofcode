from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, value

target = [3,5,4,7]
operations = [
    [0,0,0,1],
    [0,1,0,1],
    [0,0,1,0],
    [0,0,1,1],
    [1,0,1,0],
    [1,1,0,0]
]

n_ops = len(operations)
n_bits = len(target)

# Define problem
prob = LpProblem("MinButtonPresses", LpMinimize)

# Variables: number of times to press each operation
x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(n_ops)]

# Objective: minimize total presses
prob += lpSum(x)

# Constraints: sum of operations * xi = target for each bit
for j in range(n_bits):
    prob += lpSum(operations[i][j]*x[i] for i in range(n_ops)) == target[j]

# Solve
prob.solve()

# Show solution
solution = [int(value(var)) for var in x]
total_presses = sum(solution)
print("Presses per button:", solution)
print("Total presses:", total_presses)
