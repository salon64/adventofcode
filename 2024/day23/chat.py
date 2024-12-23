from collections import defaultdict
import time

start_time = time.time()

# Load input
with open('2024/day23/day_23_input.txt', 'r') as file:
    data = file.read().strip().splitlines()

# Parse connections
connections = [line.split('-') for line in data]
# print("Input connections:", connections)

computer_connections = defaultdict(set)
for comp1, comp2 in connections:
    if comp1 != comp2:
        computer_connections[comp1].add(comp2)
        computer_connections[comp2].add(comp1)

# Debug: Print graph
print("Computer connections:")
for comp, neighbors in computer_connections.items():
    print(f"{comp}: {neighbors}")

# Find unique triplets
def find_triplets(connections):
    tripplets = set()
    for node in connections:
        neighbors = list(connections[node])
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if neighbors[j] in connections[neighbors[i]]:
                    tripplet = tuple(sorted([node, neighbors[i], neighbors[j]]))
                    tripplets.add(tripplet)
                    # print("Generated Triplet:", tripplet)  # Debug
    return tripplets

tripplets = find_triplets(computer_connections)
print("Total Triplets:", len(tripplets))

# Filter triplets containing 't'
tripplets_with_t = sum(
    1 for tri in tripplets if any(comp.startswith('t') or comp.endswith('t') for comp in tri)
)
print("Triplets with 't':", tripplets_with_t)

end_time = time.time()
print(f"Time took: {round((end_time - start_time) * 1000, 2)}ms")
