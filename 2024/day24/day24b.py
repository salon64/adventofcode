from collections import defaultdict
import time
import copy
import networkx as nx
from functools import cache
from bitstring import BitArray
import matplotlib.pyplot as plt
from graphviz import Digraph
start_time = time.time()
# with open('2024/day24/day_24_input.txt', 'r') as file: # day_24_input.txt
#     data = file.read().strip().splitlines()
# print(data)
values = {}
operations = [] # source target OP destination
vals = True
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
# for val in values:
#     print(val)
# for op in operations:
#     print(f"{op},")
# print(values)
# print(operations)
values = {'x00': 1, 'x01': 1, 'x02': 0, 'x03': 0, 'x04': 0, 
          'x05': 1, 'x06': 0, 'x07': 1, 'x08': 1, 'x09': 0, 
          'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0, 'x14': 1, 
          'x15': 1, 'x16': 1, 'x17': 0, 'x18': 1, 'x19': 1, 
          'x20': 0, 'x21': 0, 'x22': 0, 'x23': 0, 'x24': 1, 
          'x25': 1, 'x26': 0, 'x27': 0, 'x28': 1, 'x29': 1, 
          'x30': 0, 'x31': 1, 'x32': 0, 'x33': 0, 'x34': 1, 
          'x35': 1, 'x36': 0, 'x37': 0, 'x38': 0, 'x39': 0, 
          'x40': 0, 'x41': 0, 'x42': 0, 'x43': 1, 'x44': 1, 
          'y00': 1, 'y01': 0, 'y02': 1, 'y03': 1, 'y04': 0, 
          'y05': 0, 'y06': 1, 'y07': 1, 'y08': 0, 'y09': 1, 
          'y10': 1, 'y11': 1, 'y12': 1, 'y13': 0, 'y14': 1, 
          'y15': 0, 'y16': 0, 'y17': 1, 'y18': 1, 'y19': 0, 
          'y20': 1, 'y21': 1, 'y22': 1, 'y23': 1, 'y24': 0, 
          'y25': 0, 'y26': 0, 'y27': 0, 'y28': 1, 'y29': 1, 
          'y30': 0, 'y31': 1, 'y32': 1, 'y33': 0, 'y34': 0, 
          'y35': 1, 'y36': 0, 'y37': 0, 'y38': 0, 'y39': 1, 
          'y40': 0, 'y41': 0, 'y42': 1, 'y43': 0, 'y44': 1}

operations = [
['fjm', 'XOR', 'gqp', 'z14'],
['x18', 'XOR', 'y18', 'hdn'],
['wbb', 'AND', 'vnp', 'shd'],
['srq', 'OR', 'mpk', 'cqw'],
['y30', 'AND', 'x30', 'tjw'],
['x26', 'AND', 'y26', 'qhf'],
['y10', 'XOR', 'x10', 'nbd'], #kbs-nbd
['y43', 'XOR', 'x43', 'swn'],
['sfj', 'OR', 'jks', 'rkg'],
['y01', 'XOR', 'x01', 'tct'],
['nsv', 'XOR', 'pjt', 'z04'],
['dcq', 'AND', 'knt', 'hfc'],
['hfh', 'AND', 'cjm', 'jks'],
['hwv', 'OR', 'cpr', 'ngm'],
['fsm', 'AND', 'btg', 'nhn'],
['y16', 'AND', 'x16', 'tqh'],
['qtf', 'XOR', 'nsp', 'z06'], # ksv-z06
['vjv', 'AND', 'vvn', 'pbj'],
['y23', 'XOR', 'x23', 'bpn'],
['tsm', 'OR', 'dnc', 'tqq'], #z20-tqq
['knt', 'XOR', 'dcq', 'z19'],
['ktj', 'AND', 'cmb', 'qqf'],
['ckh', 'OR', 'rrp', 'cmb'],
['x43', 'AND', 'y43', 'hrf'],
['mwc', 'OR', 'qjs', 'pfv'],
['qpj', 'XOR', 'vmh', 'z05'],
['y16', 'XOR', 'x16', 'dgs'],
['x29', 'XOR', 'y29', 'kcf'],
['qqf', 'OR', 'jjp', 'jmf'],
['rnp', 'XOR', 'mbj', 'z03'],
['x12', 'AND', 'y12', 'cpr'],
['x06', 'AND', 'y06', 'ksv'], # z06-ksv
['swn', 'XOR', 'rkg', 'z43'],
['x38', 'XOR', 'y38', 'fkg'],
['x04', 'XOR', 'y04', 'nsv'],
['x07', 'XOR', 'y07', 'dhf'],
['bhp', 'OR', 'shd', 'hfh'],
['pwm', 'XOR', 'jgj', 'z33'],
['ddd', 'AND', 'hdn', 'cfb'],
['qhf', 'OR', 'kqk', 'bdh'],
['tcg', 'AND', 'rtn', 'ckh'],
['mjj', 'OR', 'dcw', 'wps'],
['pjk', 'AND', 'jsv', 'sbj'],
['gfr', 'OR', 'ckc', 'vts'],
['bnp', 'AND', 'mtq', 'tsm'],
['y31', 'XOR', 'x31', 'gtq'],
['vjv', 'XOR', 'vvn', 'z44'],
['tnc', 'XOR', 'gbw', 'z09'],
['pjt', 'AND', 'nsv', 'tdr'],
['x09', 'AND', 'y09', 'gcp'],
['x19', 'XOR', 'y19', 'knt'],
['mkh', 'OR', 'pbj', 'z45'],
['bnr', 'AND', 'jhf', 'bwd'],
['x22', 'AND', 'y22', 'kkt'],
['x41', 'AND', 'y41', 'bhp'],
['x10', 'AND', 'y10', 'kbs'], # nbd-kbs
['qnn', 'AND', 'gsw', 'mjj'],
['tjw', 'OR', 'rds', 'pns'],
['y35', 'XOR', 'x35', 'srg'],
['pnj', 'XOR', 'srn', 'z26'],
['rqp', 'OR', 'qbc', 'wrd'],
['gtq', 'XOR', 'pns', 'z31'],
['y40', 'AND', 'x40', 'vpj'],
['y03', 'AND', 'x03', 'bcm'],
['dgs', 'AND', 'wps', 'ckr'],
['jwh', 'OR', 'gcp', 'dnn'], 
['sqd', 'OR', 'pvg', 'qtf'],
['cmb', 'XOR', 'ktj', 'z37'],
['vnp', 'XOR', 'wbb', 'z41'],
['bpn', 'AND', 'pjm', 'hvk'],
['cmj', 'AND', 'hpp', 'ckb'], # z39-ckb
['bnp', 'XOR', 'mtq', 'z20'], #tqq-z20
['hds', 'AND', 'cpw', 'tmk'],
['jvr', 'OR', 'kbs', 'jsv'],
['pcs', 'OR', 'kqm', 'pnj'],
['y33', 'AND', 'x33', 'jbr'],
['jww', 'XOR', 'mrf', 'z30'],
['dnn', 'XOR', 'nbd', 'z10'],
['x05', 'XOR', 'y05', 'vmh'],
['x25', 'AND', 'y25', 'pcs'],
['qbk', 'XOR', 'bpp', 'z12'],
['y25', 'XOR', 'x25', 'rpf'],
['x39', 'XOR', 'y39', 'cmj'],
['vpj', 'OR', 'nhn', 'wbb'],
['y18', 'AND', 'x18', 'djn'],
['ctm', 'XOR', 'ngm', 'z13'],
['pjb', 'AND', 'qtk', 'ckc'],
['y15', 'XOR', 'x15', 'qnn'],
['y31', 'AND', 'x31', 'nqk'],
['x02', 'XOR', 'y02', 'ndk'],
['jdv', 'XOR', 'rkk', 'z22'],
['x19', 'AND', 'y19', 'skb'],
['wrd', 'AND', 'nnd', 'tjd'],
['y07', 'AND', 'x07', 'rqp'],
['x01', 'AND', 'y01', 'mwc'],
['y03', 'XOR', 'x03', 'mbj'],
['pns', 'AND', 'gtq', 'sfd'],
['bwd', 'OR', 'bwm', 'jgj'],
['hrf', 'OR', 'grs', 'vvn'],
['y17', 'AND', 'x17', 'dmf'],
['ckr', 'OR', 'tqh', 'nbt'],
['x00', 'AND', 'y00', 'pgc'],
['tqq', 'AND', 'gmm', 'ffk'],
['x39', 'AND', 'y39', 'kqt'],
['pjm', 'XOR', 'bpn', 'z23'],
['qrm', 'OR', 'ksv', 'rrw'],
['x11', 'AND', 'y11', 'krf'],
['nbd', 'AND', 'dnn', 'jvr'],
['y30', 'XOR', 'x30', 'mrf'],
['tdr', 'OR', 'psq', 'qpj'],
['qnn', 'XOR', 'gsw', 'z15'],
['x32', 'XOR', 'y32', 'jhf'],
['wrd', 'XOR', 'nnd', 'z08'],
['x44', 'AND', 'y44', 'mkh'],
['jhf', 'XOR', 'bnr', 'z32'],
['fjm', 'AND', 'gqp', 'nbw'],
['jsv', 'XOR', 'pjk', 'z11'],
['y21', 'AND', 'x21', 'stc'],
['hwc', 'OR', 'mvv', 'rnp'],
['y13', 'AND', 'x13', 'rmd'],
['x42', 'AND', 'y42', 'sfj'],
['y15', 'AND', 'x15', 'dcw'],
['x28', 'XOR', 'y28', 'tjn'],
['x38', 'AND', 'y38', 'mrc'],
['jgj', 'AND', 'pwm', 'hqs'],
['srn', 'AND', 'pnj', 'kqk'],
['x33', 'XOR', 'y33', 'pwm'],
['tmk', 'OR', 'fmr', 'crw'],
['dhf', 'XOR', 'rrw', 'z07'],
['y28', 'AND', 'x28', 'nbj'],
['y36', 'AND', 'x36', 'rrp'],
['rkg', 'AND', 'swn', 'grs'],
['y17', 'XOR', 'x17', 'chp'],
['hfh', 'XOR', 'cjm', 'z42'],
['tnc', 'AND', 'gbw', 'jwh'],
['x37', 'XOR', 'y37', 'ktj'],
['y21', 'XOR', 'x21', 'gmm'],
['pjb', 'XOR', 'qtk', 'z34'],
['kjb', 'OR', 'nbj', 'bvh'],
['nbt', 'XOR', 'chp', 'z17'],
['rrw', 'AND', 'dhf', 'qbc'],
['pfv', 'XOR', 'ndk', 'z02'],
['y27', 'XOR', 'x27', 'bkd'],
['qpj', 'AND', 'vmh', 'sqd'],
['mrc', 'OR', 'ftb', 'hpp'],
['hvk', 'OR', 'gpq', 'cpw'],
['vts', 'XOR', 'srg', 'z35'],
['vfr', 'OR', 'kkt', 'pjm'],
['hpp', 'XOR', 'cmj', 'z39'], # ckb-z39
['y34', 'AND', 'x34', 'gfr'],
['skb', 'OR', 'hfc', 'bnp'],
['rkk', 'AND', 'jdv', 'vfr'],
['kcf', 'AND', 'bvh', 'crj'],
['ppq', 'OR', 'crj', 'jww'],
['btg', 'XOR', 'fsm', 'z40'],
['jmf', 'XOR', 'fkg', 'z38'],
['y02', 'AND', 'x02', 'mvv'],
['hdn', 'XOR', 'ddd', 'z18'],
['ffk', 'OR', 'stc', 'rkk'],
['x44', 'XOR', 'y44', 'vjv'],
['y08', 'AND', 'x08', 'vsw'],
['tjd', 'OR', 'vsw', 'tnc'],
['pvc', 'OR', 'nbw', 'gsw'],
['y42', 'XOR', 'x42', 'cjm'],
['x06', 'XOR', 'y06', 'nsp'], 
['kcf', 'XOR', 'bvh', 'z29'],
['y05', 'AND', 'x05', 'pvg'],
['x36', 'XOR', 'y36', 'rtn'],
['y24', 'AND', 'x24', 'fmr'],
['mbj', 'AND', 'rnp', 'ppp'],
['crw', 'AND', 'rpf', 'kqm'],
['cpw', 'XOR', 'hds', 'z24'],
['pgc', 'XOR', 'tct', 'z01'],
['ndk', 'AND', 'pfv', 'hwc'],
['x14', 'XOR', 'y14', 'gqp'],
['qtf', 'AND', 'nsp', 'qrm'],
['tct', 'AND', 'pgc', 'qjs'],
['rmd', 'OR', 'wdq', 'fjm'],
['x20', 'AND', 'y20', 'dnc'],
['y13', 'XOR', 'x13', 'ctm'],
['nbt', 'AND', 'chp', 'cbf'],
['x40', 'XOR', 'y40', 'fsm'],
['x32', 'AND', 'y32', 'bwm'],
['jww', 'AND', 'mrf', 'rds'],
['x00', 'XOR', 'y00', 'z00'],
['dmf', 'OR', 'cbf', 'ddd'],
['x29', 'AND', 'y29', 'ppq'],
['crw', 'XOR', 'rpf', 'z25'],
['qbk', 'AND', 'bpp', 'hwv'],
['y11', 'XOR', 'x11', 'pjk'],
['bdh', 'AND', 'bkd', 'mpk'],
['wps', 'XOR', 'dgs', 'z16'],
['sbj', 'OR', 'krf', 'bpp'],
['kqt', 'OR', 'ckb', 'btg'],
['x12', 'XOR', 'y12', 'qbk'],
['y26', 'XOR', 'x26', 'srn'],
['y34', 'XOR', 'x34', 'qtk'],
['cqw', 'XOR', 'tjn', 'z28'],
['sfd', 'OR', 'nqk', 'bnr'],
['hqs', 'OR', 'jbr', 'pjb'],
['y08', 'XOR', 'x08', 'nnd'],
['bdh', 'XOR', 'bkd', 'z27'],
['y37', 'AND', 'x37', 'jjp'],
['tcg', 'XOR', 'rtn', 'z36'],
['x04', 'AND', 'y04', 'psq'],
['gmm', 'XOR', 'tqq', 'z21'],
['bgp', 'OR', 'ntc', 'tcg'],
['ngm', 'AND', 'ctm', 'wdq'],
['y35', 'AND', 'x35', 'bgp'],
['y23', 'AND', 'x23', 'gpq'],
['vts', 'AND', 'srg', 'ntc'],
['x09', 'XOR', 'y09', 'gbw'],
['y41', 'XOR', 'x41', 'vnp'],
['x22', 'XOR', 'y22', 'jdv'],
['y20', 'XOR', 'x20', 'mtq'],
['x24', 'XOR', 'y24', 'hds'],
['cfb', 'OR', 'djn', 'dcq'],
['jmf', 'AND', 'fkg', 'ftb'],
['ppp', 'OR', 'bcm', 'pjt'],
['y27', 'AND', 'x27', 'srq'],
['tjn', 'AND', 'cqw', 'kjb'],
['y14', 'AND', 'x14', 'pvc'],
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

def is_correct_state(result_):
    x_values = reversed(sorted([(k, v) for k, v in result_.items() if k.startswith("x")]))
    x_binary_string = ''.join(str(v[1]) for v in x_values)
    x_binary_result = BitArray(bin=x_binary_string).uint
    y_values = reversed(sorted([(k, v) for k, v in result_.items() if k.startswith("y")]))
    y_binary_string = ''.join(str(v[1]) for v in y_values)
    y_binary_result = BitArray(bin=y_binary_string).uint
    z_values = reversed(sorted([(k, v) for k, v in result_.items() if k.startswith("z")]))
    z_binary_string = ''.join(str(v[1]) for v in z_values)
    z_binary_result = BitArray(bin=z_binary_string).uint

    resxy = x_binary_result + y_binary_result
    resxy_binary_string = bin(resxy)[2:]  
    rez_bin = BitArray(bin=resxy_binary_string).uint

    # print(f"{resxy_binary_string}: {resxy}")
    # print(f"{z_binary_string}: {z_binary_result}")
    return x_binary_result + y_binary_result == z_binary_result

print(is_correct_state(result))

def visualize_graph_with_graphviz():
    # Create a directed graph
    dot = Digraph(format='png')  # Use 'png' or any other supported format

    # Add regular nodes with computed values
    for node in graph.nodes:
        label = f"{node}\n{values.get(node, '')}"  # Node label with name and value
        dot.node(node, label=label, shape="ellipse", style="filled", fillcolor="lightblue")

    # Dictionary to track seen operation-destination pairs
    operation_map = {}
    operation_count = 0  # Unique identifier for operation nodes
    
    # Create operation bubbles and edges
    for u, v, data in graph.edges(data=True):
        operation = data.get("operation", "")

        if operation:  # If there's an operation
            # Check if this operation-destination pair already exists
            op_dest_pair = (operation, v)
            if op_dest_pair not in operation_map:
                # If not, create a new operation node and map it
                operation_node = f"op_{operation_count}"
                operation_map[op_dest_pair] = operation_node
                operation_count += 1

                # Add the operation bubble
                dot.node(operation_node, label=operation, shape="circle", style="filled", fillcolor="lightgrey")
            else:
                # Use the existing operation node
                operation_node = operation_map[op_dest_pair]

            # Connect inputs to the operation bubble
            dot.edge(u, operation_node)

            # Connect the operation bubble to the output
            dot.edge(operation_node, v)
        else:
            # Directly connect nodes if no operation is specified
            dot.edge(u, v)

    # Render the graph
    output_path = "2024/day24/graph_output"
    dot.render(output_path, cleanup=True)  # Saves as 2024/day24/graph_output.png


# visualize_graph_with_graphviz()
# 1111 False
# 2111 False
# 2211 False
# 2221 False
# 2121 True

# 6  : (z06 - nsp) or (z06 - ksv)
# 10 : (nbd - kbs) or (dnn - kbs)
# 20 : (tsm - tqq) or (z20 - tqq)
# 39 : (ckb-z39) 

# ksv-z06 2
# kbs-nbd 1
# tqq-z20 2
# ckb-z39 1
# ckb,kbs,ksv,nbd,tqq,z06,z20,z39
print(['ckb','kbs','ksv','nbd','tqq','z06','z20','z39'])