import networkx as nx
with open('2025/day11/day_11_input.txt', 'r') as file:
    data = file.read().strip()

G = nx.DiGraph()

for line in data.splitlines():
    line = line.strip()
    if not line:
        continue
    src, rhs = line.split(":", 1)
    src = src.strip()
    targets = [t for t in rhs.split() if t]
    if targets:
        for dst in targets:
            G.add_edge(src, dst)
    else:
        G.add_node(src)

count = sum(1 for _ in nx.all_simple_paths(G, "you", "out"))
print(count)