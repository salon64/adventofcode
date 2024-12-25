import time
import networkx as nx
from functools import cache
start_time = time.time()
with open('2024/day21/test', 'r') as file: # day_21_input.txt
    data = file.read().strip().splitlines()

codes = [list(line) for line in data]
print(codes)
# expected moves fore 029A, len = 68
# print(len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"))

#   terminal             r1               r2                    user
# +---+---+---+  #     +---+---+  #     +---+---+              +---+---+
# | 7 | 8 | 9 |  #     | ^ | A |  #     | ^ | A |              | ^ | A |
# +---+---+---+  # +---+---+---+  # +---+---+---+   user:  +---+---+---+
# | 4 | 5 | 6 |  # | < | v | > |  # | < | v | > |          | < | v | > | 
# +---+---+---+  # +---+---+---+  # +---+---+---+          +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

numeric = nx.DiGraph()
numeric.add_edges_from([("A", "0"), ("A", "3")])
numeric.add_edges_from([("0", "2"), ("0", "A")])
numeric.add_edges_from([("1", "4"), ("1", "2")])
numeric.add_edges_from([("2", "1"), ("2", "5"), ("2", "3"), ("2", "0")])
numeric.add_edges_from([("3", "2"), ("3", "6"), ("3", "A")])
numeric.add_edges_from([("4", "7"), ("4", "5"), ("4", "1")])
numeric.add_edges_from([("5", "4"), ("5", "8"), ("5", "6"), ("5", "2")])
numeric.add_edges_from([("6", "5"), ("6", "9"), ("6", "3")])
numeric.add_edges_from([("7", "8"), ("7", "4")])
numeric.add_edges_from([("8", "7"), ("8", "5"), ("8", "9")])
numeric.add_edges_from([("9", "8"), ("9", "6")])

numeric_move = {
    ('A', '0'): '<', ('A', '3'): '^',
    ('0', '2'): '^', ('0', 'A'): '>',
    ('1', '4'): '^', ('1', '2'): '>', 
    ('2', '1'): '<', ('2', '5'): '^', ('2', '3'): '>', ('2', '0'): 'v',
    ('3', '2'): '<', ('3', '6'): '^', ('3', 'A'): 'v', 
    ('4', '7'): '^', ('4', '5'): '>', ('4', '1'): 'v', 
    ('5', '4'): '<', ('5', '8'): '^', ('5', '6'): '>', ('5', '2'): 'v', 
    ('6', '5'): '<', ('6', '9'): '^', ('6', '3'): 'v',
    ('7', '8'): '>', ('7', '4'): 'v', 
    ('8', '7'): '<', ('8', '5'): 'v', ('8', '9'): '>', 
    ('9', '8'): '<', ('9', '6'): 'v'
}

directional = nx.DiGraph()
directional.add_edges_from([("A", "^"), ("A", ">")])
directional.add_edges_from([("^", "A"), ("^", "v")])
directional.add_edges_from([("<", "v")])
directional.add_edges_from([("v", "<"), ("v", "^"), ("v", ">")])
directional.add_edges_from([(">", "v"), (">", "A")])

directional_move = {
    ('A', '^'): "<", ('A', '>'): "v",
    ('^', 'A'): ">", ('^', 'v'): "v",
    ('<', 'v'): ">",
    ('v', '<'): "<", ('v', '^'): "^", ('v', '>'): ">",
    ('>', 'v'): "<", ('>', 'A'): "^",
}








end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

