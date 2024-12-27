from collections import defaultdict
import time
import networkx as nx
from functools import cache
import re
start_time = time.time()
with open('2024/day21/day_21_input.txt', 'r') as file: # day_21_input.txt
    data = file.read().strip().splitlines()
# print(codes)
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

def paths_numeric(A,B):
    paths = []
    for p in nx.all_shortest_paths(numeric,A,B):
        seq = []
        for i in range(len(p)-1):
            move = (p[i],p[i+1])
            seq += [ numeric_move[move] ]
        seq += ['A'] # press A
        paths.append("".join(seq))
    return paths

def solve_numeric(code):
    paths = []
    _code = "A"+code
    for i in range(len(_code)-1):
        paths.append(paths_numeric(_code[i],_code[i+1]))
    sequences = [""]
    i = 0
    while i<len(paths):
        sequences_new = []
        for s in sequences:
            for p in paths[i]:
                sequences_new.append(s+p)
        sequences = sequences_new
        i+=1
    return sequences
# code = "029A"
# print(solve_numeric(code))

def paths_directional(A,B):
    paths = []
    for p in nx.all_shortest_paths(directional,A,B):
        seq = []
        for i in range(len(p)-1):
            move = (p[i],p[i+1])
            seq += [ directional_move[move] ]
        seq += ['A'] # press A
        paths.append("".join(seq))
    return paths

def solve_directional(code):
    paths = []
    _code = "A"+code
    for i in range(len(_code)-1):
        paths.append(paths_directional(_code[i],_code[i+1]))
    sequences = [""]
    i = 0
    while i<len(paths):
        sequences_new = []
        for s in sequences:
            for p in paths[i]:
                sequences_new.append(s+p)
        sequences = sequences_new
        i+=1
    return sequences
# code = "<A^A>^^AvvvA"
# print(solve_directional(code))



# original solution:
# def solve_code(code):
#     solutions = []
#     for key1 in solve_numeric(code):
#         for key2 in solve_directional(key1):
#             for key3 in solve_directional(key2):
#                 solutions.append(key3)
#     return min(solutions,key=len)
# solve_code_("029A")
# result = 0
# for code in data:
#     tmp = int(re.search(r'\d+', code).group())
#     tmp2 = solve_code(code)
#     result += len(tmp2) * tmp
#     # print(code, solve_code(code))
#     # print(f"{len(tmp2)} * {tmp}")
# print(result)

def find_shortest_paths(G,Gmove):
    paths = defaultdict(list)
    for start in G.nodes():
        for end in G.nodes():
            if start != end:
                for p in list(nx.all_shortest_paths(G, start, end)):
                    m = "".join([ Gmove[(p[i],p[i+1])] for i in range(len(p)-1) ])
                    paths[ start+end ].append(m)
    return paths
numerc_paths = find_shortest_paths(numeric, numeric_move)
directional_paths = find_shortest_paths(directional,directional_move)

@cache
def minimum_sequence(level, code, nrobots):
    # end of keypad sequence reached, return lenght of current sequence 
    if level == nrobots + 1:
        return len(code)

    # select dictionary of shortest paths according to level and corresponding keypad
    if level==0:
        paths = numerc_paths
    else:
        paths = directional_paths

    # recursively cumulate sequence lenght, only considering shortest one
    total = 0
    for start, end in zip('A'+code, code):
        # adding "A" command at end of current step to press the button!
        min_seq = [ minimum_sequence(level+1, p+"A", nrobots) for p in paths[ start+end ] ]
        if min_seq:
            total += min(min_seq)
        else:
            # When the same button is pressed twice in a row account for 1 step in sequence,
            # since  min_seq would be empty (no entry in the shortest path dictionaries), but
            # operation is happening anyway
            total += 1 

    return total
# minimum_sequence(0, "029A", 2)

result = 0
for code in data:
    tmp = int(re.search(r'\d+', code).group())
    tmp2 = minimum_sequence(0, code, 2)
    result += tmp2 * tmp
print(result)


end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

