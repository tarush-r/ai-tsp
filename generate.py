import numpy as np


def generate_tsp_instance(n):
    # Create a random matrix with positive values in [0, 100]
    distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance_matrix[i][j] = distance_matrix[j][i] = np.random.uniform() * 100

    # Set diagonal elements to 0
    for i in range(n):
        distance_matrix[i][i] = 0.0

    return distance_matrix
