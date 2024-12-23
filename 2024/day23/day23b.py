import time
import networkx as nx
start_time = time.time()
with open('2024/day23/day_23_input.txt', 'r') as file: # day_23_input.txt
    data = file.read().strip().splitlines()

G = nx.Graph()
for line in data:
    l, r = line.split('-')
    G.add_edge(l, r)

largest_clique = []
for clique in nx.enumerate_all_cliques(G):
    largest_clique = clique  # overwrite with the latest (largest) clique
print(",".join(sorted(largest_clique)))

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')