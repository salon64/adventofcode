from collections import defaultdict
import time
import copy
import networkx as nx
from functools import cache
from bitstring import BitArray
import matplotlib.pyplot as plt
from graphviz import Digraph
start_time = time.time()
with open('2024/day24/day_24_input.txt', 'r') as file: # day_24_input.txt
    data = file.read().strip().splitlines()
# print(data)
values = {}
operations = [] # source target OP destination
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
# print(values)
# print(operations)

graph = nx.DiGraph() # directed acyclic graph
for src, op, tar, des in operations:
    graph.add_edge(src, des, operation=op)
    graph.add_edge(tar, des, operation=op)

def compute(op, inputs):
    if op == 'XOR':
        return inputs[0] ^ inputs[1]
    elif op == 'OR':
        return inputs[0] | inputs[1]
    elif op == 'AND':
        return inputs[0] & inputs[1]
    
def get_values(graph, values):
    for node in nx.topological_sort(graph):
        if node not in values:
            sources = list(graph.predecessors(node))
            if sources:
                operation = graph.edges[sources[0], node]["operation"]
                input_values = [values[pred] for pred in sources]
                values[node] = compute(operation, input_values)
    return values

def is_correct_state(graph, values):
    result = get_values(graph, values)

    x_values = reversed(sorted([(k, v) for k, v in result.items() if k.startswith("x")]))
    x_binary_string = ''.join(str(v[1]) for v in x_values)
    x_binary_result = BitArray(bin=x_binary_string).uint
    y_values = reversed(sorted([(k, v) for k, v in result.items() if k.startswith("y")]))
    y_binary_string = ''.join(str(v[1]) for v in y_values)
    y_binary_result = BitArray(bin=y_binary_string).uint
    z_values = reversed(sorted([(k, v) for k, v in result.items() if k.startswith("z")]))
    z_binary_string = ''.join(str(v[1]) for v in z_values)
    z_binary_result = BitArray(bin=z_binary_string).uint

    resxy = x_binary_result + y_binary_result
    resxy_binary_string = bin(resxy)[2:]  
    rez_bin = BitArray(bin=resxy_binary_string).uint

    # print(f"{x_binary_string}: {x_binary_result}")
    # print(f"{y_binary_string}: {y_binary_result}")
    # print()
    # print(f"{resxy_binary_string}: {resxy}")
    # print(f"{z_binary_string}: {y_binary_result}")

    return x_binary_result + y_binary_result == z_binary_result




def swap_em():
    edges = list(graph.edges(data=True))
    edge_pairs = defaultdict(list)
    for edge in edges:
        src, des, op = edge
        edge_pairs[des].append(src)
        



































# print(z_binary_string)
# print(z_binary_result)

# def visualize_graph_with_graphviz(graph, values):
#     # Create a directed graph
#     dot = Digraph(format='png')  # Use 'png' or any other supported format

#     # Add nodes with computed values
#     for node in graph.nodes:
#         label = f"{node}\n{values.get(node, '')}"  # Node label with name and value
#         dot.node(node, label=label, shape="ellipse", style="filled", fillcolor="lightblue")

#     # Add edges with operations
#     for u, v, data in graph.edges(data=True):
#         operation = data.get("operation", "")
#         dot.edge(u, v, label=operation)

#     # Render the graph
#     output_path = "2024/day24/graph_output"
#     dot.render(output_path, cleanup=True)  # Saves as 2024/day24/graph_output.png

# visualize_graph_with_graphviz(graph, result)



end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

