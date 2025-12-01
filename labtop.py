from z3 import *

A = Int('A')
B = Int('B')
C = Int('C')
D = Int('D')
E = Int('E')
F = Int('F')
G = Int('G')
H = Int('H')
I = Int('I')
J = Int('J')
K = Int('K')
L = Int('L')
M = Int('M')
N = Int('N')
O = Int('O')
P = Int('P')

relations = [
    [F, D, '-', '<', -1],
    [L, A, '-', '==', -5],
    [E, M, '^', '==', 2],
    [N, B, '^', '==', 19],
    [K, B, '|', '==', 126],
    [H, E, '|', '==', 108],
    [P, G, '^', '==', 16],
    [I, J, '^', '==', 9],
    [C, L, '+', '==', 226],
    [O, D, '-', '==', -5],
    [I, H, '|', '==', 128],
    [D, L, '+', '<', 226],
    [F, J, '^', '==', 8],
    [L, K, '|', '==', 111],
    [B, D, '^', '==', 2],
    [M, C, '^', '==', 25],
    [J, P, '^', '==', 26]
]

s = Solver()

for rel in relations:
    if rel[2] == "+":
        if rel[3] == "==":
            s.add

    if rel[2] == "+":
        if rel[3] == "==":
            s.add(rel[0] + rel[1] == rel[4])
        elif rel[3] == "<":
            s.add(rel[0] + rel[1] < rel[4])
    elif rel[2] == "-":
        if rel[3] == "==":
            s.add(rel[0] - rel[1] == rel[4])
        elif rel[3] == "<":
            s.add(rel[0] - rel[1] < rel[4])
    elif rel[2] == "^":
        if rel[3] == "==":
            s.add(rel[0] ^ rel[1] == rel[4])
    elif rel[2] == "|":
        if rel[3] == "==":
            s.add(rel[0] | rel[1] == rel[4])

if s.check() == sat:
    print(s.model())
else:
    print("No solution")