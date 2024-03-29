from structs import *
from algos.brute_force import bruteForce
from algos.b_and_b import branchAndBound
from algos.sls import sls
if __name__ == "__main__":
    graph = Graph([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])

    graph = Graph([
        [0, 0.5, 1, 10],
        [0.5, 0, 5, 2],
        [1, 5, 0, 3],
        [10, 2, 3, 0]
    ])

    graph = Graph([
        [0.0000, 0.5303, 0.1727, 2.7942, 2.3385, 1.9787, 0.6226, 0.7087, 1.3965, 0.7403],
        [0.5303, 0.0000, 1.6619, 1.7715, 0.3817, 0.5030, 0.0054, 0.3665, 1.0130, 0.9184],
        [0.1727, 1.6619, 0.0000, 0.0881, 1.3253, 1.5245, 0.9192, 1.8067, 0.4636, 0.8676],
        [2.7942, 1.7715, 0.0881, 0.0000, 1.2906, 1.7981, 0.2393, 0.0672, 0.8743, 1.1939],
        [2.3385, 0.3817, 1.3253, 1.2906, 0.0000, 0.3020, 0.7884, 0.0550, 0.5590, 1.3183],
        [1.9787, 0.5030, 1.5245, 1.7981, 0.3020, 0.0000, 1.0629, 0.6247, 1.6497, 0.4459],
        [0.6226, 0.0054, 0.9192, 0.2393, 0.7884, 1.0629, 0.0000, 0.5316, 0.4628, 0.7779],
        [0.7087, 0.3665, 1.8067, 0.0672, 0.0550, 0.6247, 0.5316, 0.0000, 1.3560, 0.0458],
        [1.3965, 1.0130, 0.4636, 0.8743, 0.5590, 1.6497, 0.4628, 1.3560, 0.0000, 0.7441],
        [0.7403, 0.9184, 0.8676, 1.1939, 1.3183, 0.4459, 0.7779, 0.0458, 0.7441, 0.0000]
    ])

    print(bruteForce(graph))
    print(branchAndBound(graph))
    print(sls(graph))
