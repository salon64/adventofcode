from collections import defaultdict
import time
import copy
import networkx as nx
from functools import cache
from bitstring import BitArray
start_time = time.time()
with open('2024/day24/test', 'r') as file: # day_24_input.txt
    data = file.read().strip().splitlines()
# print(data)
values = {}
operations = [] # source target OP destination


def solve(values, operations):
    # do the cool stuff
    las_op_len = len(operations)
    while operations:
        i = 0
        while i in range(0, len(operations)):
            s, op, t, d = operations[i]
            # print(f"s: {s}, t: {t}, op: {op}, d: {d}")
            if values.setdefault(s, -1) != -1 and values.setdefault(t, -1) != -1:
                if op == 'AND':
                    values[d] = values[s] & values[t]
                elif op == 'OR':
                    values[d] = values[s] | values[t]
                elif op == 'XOR':
                    values[d] = values[s] ^ values[t]
                operations.pop(i) # operation finished
            else:
                i += 1

            if i > len(operations):
                i = 0
            if operations == []:
                break
        
        if len(operations) == las_op_len:
            print("failed")
            return False
        else:
            las_op_len = len(operations)
    return True

vals = True
for line in data:
    if line == '':
        vals = False
        continue
    if vals:
        values[line[:3]] = int(line[-1])
    elif not vals:
        tmp = line.split(' ')
        tmp.pop(3)
        operations.append(tmp)
print(values)
print(operations)

for i, op1 in enumerate(operations):
    for j, op2 in enumerate(operations):
        if i != j:
            swapped = []
            print(f"{op1[3]}, {op2[3]}")
            op1[3], op2[3] = op2[3], op1[3]
            print(f"{op1[3]}, {op2[3]}")
            print()
            # swap back
            op1[3], op2[3] = op2[3], op1[3]
            # solve(values, operations)
        































# z_values = sorted([(k, v) for k, v in values.items() if k.startswith("z")])
# binary_string = ''.join(str(v[1]) for v in z_values)
# reversed_binary_string = binary_string[::-1]
# reversed_binary_result = BitArray(bin=reversed_binary_string).uint

# print(reversed_binary_string)
# print(reversed_binary_result)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')


# graph = nx.DiGraph() # directed acyclic graph
# for src, op, tar, des in operations:
#     graph.add_edge(src, des, operation=op)
#     graph.add_edge(tar, des, operation=op)

# def compute(op, inputs):
#     if op == 'XOR':
#         return inputs[0] ^ inputs[1]
#     elif op == 'OR':
#         return inputs[0] | inputs[1]
#     elif op == 'AND':
#         return inputs[0] & inputs[1]
    
# def get_values(graph, values):
#     for node in nx.topological_sort(graph):
#         if node not in values:
#             sources = list(graph.predecessors(node))
#             if sources:
#                 operation = graph.edges[sources[0], node]["operation"]
#                 input_values = [values[pred] for pred in sources]
#                 values[node] = compute(operation, input_values)
#     return values

# result = get_values(graph, values)