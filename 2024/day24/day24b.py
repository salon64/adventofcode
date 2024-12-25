from collections import defaultdict
import time
import copy
import networkx as nx
from functools import cache
from bitstring import BitArray
import matplotlib.pyplot as plt
from graphviz import Digraph
start_time = time.time()
# with open('2024/day24/test', 'r') as file: # day_24_input.txt
#     data = file.read().strip().splitlines()
# print(data)
# values = {}
# operations = [] # source target OP destination
# vals = True
# for line in data:
#     if line == '':
#         vals = False
#         continue
#     if vals:
#         values[line[:3]] = int(line[-1])
#     elif not vals:
#         tmp = line.split(' ')
#         tmp.pop(3)
#         operations.append(tmp)

values = {
    "x00": 1, "x01": 1, "x02": 0, "x03": 0, "x04": 0,
    "x05": 1, "x06": 0, "x07": 1, "x08": 1, "x09": 0,
    "x10": 1, "x11": 0, "x12": 0, "x13": 0, "x14": 1,
    "x15": 1, "x16": 1, "x17": 0, "x18": 1, "x19": 1,
    "x20": 0, "x21": 0, "x22": 0, "x23": 0, "x24": 1,
    "x25": 1, "x26": 0, "x27": 0, "x28": 1, "x29": 1,
    "x30": 0, "x31": 1, "x32": 0, "x33": 0, "x34": 1,
    "x35": 1, "x36": 0, "x37": 0, "x38": 0, "x39": 0,
    "x40": 0, "x41": 0, "x42": 0, "x43": 1, "x44": 1,
    "y00": 1, "y01": 0, "y02": 1, "y03": 1, "y04": 0,
    "y05": 0, "y06": 1, "y07": 1, "y08": 0, "y09": 1,
    "y10": 1, "y11": 1, "y12": 1, "y13": 0, "y14": 1,
    "y15": 0, "y16": 0, "y17": 1, "y18": 1, "y19": 0,
    "y20": 1, "y21": 1, "y22": 1, "y23": 1, "y24": 0,
    "y25": 0, "y26": 0, "y27": 0, "y28": 1, "y29": 1,
    "y30": 0, "y31": 1, "y32": 1, "y33": 0, "y34": 0,
    "y35": 1, "y36": 0, "y37": 0, "y38": 0, "y39": 1,
    "y40": 0, "y41": 0, "y42": 1, "y43": 0, "y44": 1
}

operations = [
    ("fjm", "gqp", "z14", "XOR"),
    ("x18", "y18", "hdn", "XOR"),
    ("wbb", "vnp", "shd", "AND"),
    ("srq", "mpk", "cqw", "OR"),
    ("y30", "x30", "tjw", "AND"),
    ("x26", "y26", "qhf", "AND"),
    ("y10", "x10", "kbs", "XOR"),
    ("y43", "x43", "swn", "XOR"),
    ("sfj", "jks", "rkg", "OR"),
    ("y01", "x01", "tct", "XOR"),
    ("nsv", "pjt", "z04", "XOR"),
    ("dcq", "knt", "hfc", "AND"),
    ("hfh", "cjm", "jks", "AND"),
    ("hwv", "cpr", "ngm", "OR"),
    ("fsm", "btg", "nhn", "AND"),
    ("y16", "x16", "tqh", "AND"),
    ("qtf", "nsp", "ksv", "XOR"),
    ("vjv", "vvn", "pbj", "AND"),
    ("y23", "x23", "bpn", "XOR"),
    ("tsm", "dnc", "z20", "OR"),
    ("knt", "dcq", "z19", "XOR"),
    ("ktj", "cmb", "qqf", "AND"),
    ("ckh", "rrp", "cmb", "OR"),
    ("x43", "y43", "hrf", "AND"),
    ("mwc", "qjs", "pfv", "OR"),
    ("qpj", "vmh", "z05", "XOR"),
    ("y16", "x16", "dgs", "XOR"),
    ("x29", "y29", "kcf", "XOR"),
    ("qqf", "jjp", "jmf", "OR"),
    ("rnp", "mbj", "z03", "XOR"),
    ("x12", "y12", "cpr", "AND"),
    ("x06", "y06", "z06", "AND"),
    ("swn", "rkg", "z43", "XOR"),
    ("x38", "y38", "fkg", "XOR"),
    ("x04", "y04", "nsv", "XOR"),
    ("x07", "y07", "dhf", "XOR"),
    ("bhp", "shd", "hfh", "OR"),
    ("pwm", "jgj", "z33", "XOR"),
    ("ddd", "hdn", "cfb", "AND"),
    ("qhf", "kqk", "bdh", "OR"),
    ("tcg", "rtn", "ckh", "AND"),
    ("mjj", "dcw", "wps", "OR"),
    ("pjk", "jsv", "sbj", "AND"),
    ("gfr", "ckc", "vts", "OR"),
    ("bnp", "mtq", "tsm", "AND"),
    ("y31", "x31", "gtq", "XOR"),
    ("vjv", "vvn", "z44", "XOR"),
    ("tnc", "gbw", "z09", "XOR"),
    ("pjt", "nsv", "tdr", "AND"),
    ("x09", "y09", "gcp", "AND"),
    ("x19", "y19", "knt", "XOR"),
    ("mkh", "pbj", "z45", "OR"),
    ("bnr", "jhf", "bwd", "AND"),
    ("x22", "y22", "kkt", "AND"),
    ("x41", "y41", "bhp", "AND"),
    ("x10", "y10", "nbd", "AND"),
    ("qnn", "gsw", "mjj", "AND"),
    ("tjw", "rds", "pns", "OR"),
    ("y35", "x35", "srg", "XOR"),
    ("pnj", "srn", "z26", "XOR"),
    ("rqp", "qbc", "wrd", "OR"),
    ("gtq", "pns", "z31", "XOR"),
    ("y40", "x40", "vpj", "AND"),
    ("y03", "x03", "bcm", "AND"),
    ("dgs", "wps", "ckr", "AND"),
    ("jwh", "gcp", "dnn", "OR"),
    ("sqd", "pvg", "qtf", "OR"),
    ("cmb", "ktj", "z37", "XOR"),
    ("vnp", "wbb", "z41", "XOR"),
    ("bpn", "pjm", "hvk", "AND"),
    ("cmj", "hpp", "z39", "AND"),
    ("bnp", "mtq", "tqq", "XOR"),
    ("hds", "cpw", "tmk", "AND"),
    ("jvr", "kbs", "jsv", "OR"),
    ("pcs", "kqm", "pnj", "OR"),
    ("y33", "x33", "jbr", "AND"),
    ("jww", "mrf", "z30", "XOR"),
    ("dnn", "nbd", "z10", "XOR"),
    ("x05", "y05", "vmh", "XOR"),
    ("x25", "y25", "pcs", "AND"),
    ("qbk", "bpp", "z12", "XOR"),
    ("y25", "x25", "rpf", "XOR"),
    ("x39", "y39", "cmj", "XOR"),
    ("vpj", "nhn", "wbb", "OR"),
    ("y18", "x18", "djn", "AND"),
    ("ctm", "ngm", "z13", "XOR"),
    ("pjb", "qtk", "ckc", "AND"),
    ("y15", "x15", "qnn", "XOR"),
    ("y31", "x31", "nqk", "AND"),
    ("x02", "y02", "ndk", "XOR"),
    ("jdv", "rkk", "z22", "XOR"),
    ("x19", "y19", "skb", "AND"),
    ("wrd", "nnd", "tjd", "AND"),
    ("y07", "x07", "rqp", "AND"),
    ("x01", "y01", "mwc", "AND"),
    ("y03", "x03", "mbj", "XOR"),
    ("pns", "gtq", "sfd", "AND"),
    ("bwd", "bwm", "jgj", "OR"),
    ("hrf", "grs", "vvn", "OR"),
    ("y17", "x17", "dmf", "AND"),
    ("ckr", "tqh", "nbt", "OR"),
    ("x00", "y00", "pgc", "AND"),
    ("tqq", "gmm", "ffk", "AND"),
    ("x39", "y39", "kqt", "AND"),
    ("pjm", "bpn", "z23", "XOR"),
    ("qrm", "ksv", "rrw", "OR"),
    ("x11", "y11", "krf", "AND"),
    ("nbd", "dnn", "jvr", "AND"),
    ("y30", "x30", "mrf", "XOR"),
    ("tdr", "psq", "qpj", "OR"),
    ("qnn", "gsw", "z15", "XOR"),
    ("x32", "y32", "jhf", "XOR"),
    ("wrd", "nnd", "z08", "XOR"),
    ("x44", "y44", "mkh", "AND"),
    ("jhf", "bnr", "z32", "XOR")
]






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

result = get_values(graph, values)




z_values = sorted([(k, v) for k, v in result.items() if k.startswith("z")])
binary_string = ''.join(str(v[1]) for v in z_values)
reversed_binary_string = binary_string[::-1]
reversed_binary_result = BitArray(bin=reversed_binary_string).uint

print(reversed_binary_string)
print(reversed_binary_result)

def visualize_graph_with_graphviz(graph, values):
    # Create a directed graph
    dot = Digraph(format='png')  # Use 'png' or any other supported format

    # Add nodes with computed values
    for node in graph.nodes:
        label = f"{node}\n{values.get(node, '')}"  # Node label with name and value
        dot.node(node, label=label, shape="ellipse", style="filled", fillcolor="lightblue")

    # Add edges with operations
    for u, v, data in graph.edges(data=True):
        operation = data.get("operation", "")
        dot.edge(u, v, label=operation)

    # Render the graph
    output_path = "2024/day24/graph_output"
    dot.render(output_path, cleanup=True)  # Saves as 2024/day24/graph_output.png

visualize_graph_with_graphviz(graph, result)



end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

