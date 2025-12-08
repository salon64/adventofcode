import numpy as np
from scipy.spatial.distance import cdist

with open('2025/day8/day_8_input.txt', 'r') as file:
    data = file.read().strip()

rows = [list(map(int, line.split(','))) for line in data.split('\n')]
X = np.array(rows)

def find_circuits(X, k):
    n_points = len(X)
    circuits = [[i] for i in range(n_points)]
    # point index to circuit index
    point_to_circuit = {i: i for i in range(n_points)}
    
    distances = cdist(X, X, metric='euclidean')
    np.fill_diagonal(distances, np.inf)
    
    connections_made = 0
    while connections_made < k:
        min_idx = np.argmin(distances)
        i, j = np.unravel_index(min_idx, distances.shape)

        if connections_made == 5518:
            # print(X[i], X[j])
            print(X[i][0] * X[j][0])
        
        if distances[i, j] == np.inf:
            break
        
        circuit_i = point_to_circuit[i]
        circuit_j = point_to_circuit[j]

        if circuit_i != circuit_j:
            circuits[circuit_i].extend(circuits[circuit_j])

            for point in circuits[circuit_j]:
                point_to_circuit[point] = circuit_i
            
            circuits[circuit_j] = []
            
            # print(f"Connected points {i} and {j}")
        
        connections_made += 1
        distances[i, j] = np.inf
        distances[j, i] = np.inf
        # print(f"conncections made: {connections_made}, circuits: {circuits}")
        over_zero = 0
        for c in circuits:
            if len(c) > 0:
                over_zero += 1
        if over_zero == 1:
            # print(connections_made)
            break
    
    final_circuits = [c for c in circuits if len(c) > 0]
    return final_circuits

circuits = find_circuits(X, 10000)