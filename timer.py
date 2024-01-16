import time
from algos.b_and_b import branchAndBound
from algos.brute_force import bruteForce
from algos.sls import sls
from generate import generate_tsp_instance
from structs import Graph

MAX_N = 20
NUM_TRIALS = 5      # Number of TSP runs per `n`

def time_tsp(algo_f, graph):
    t_start = time.time_ns()
    for _ in range(NUM_TRIALS):
        algo_f(graph)
    t_end = time.time_ns()
    return (t_end - t_start) / 10**6

def write_header(f):
    f.write(f"n,bruteForce,branchAndBound,sls\n")

def write_times(f, n, avgs):
    f.write(f"{n},{avgs['bruteForce']},{avgs['branchAndBound']},{avgs['sls']}\n")

if __name__ == "__main__":
    # Average time in ms
    avgs = {
        "bruteForce": 0,
        "branchAndBound": 0,
        "sls": 0
    }

    f = open("times.csv", "a")
    write_header(f)

    for n in range(3, MAX_N + 1):
        graph = Graph(generate_tsp_instance(n))

        avgs["bruteForce"] = round(time_tsp(bruteForce, graph) / NUM_TRIALS, 4)
        # avgs["branchAndBound"] = round(time_tsp(branchAndBound, graph) / NUM_TRIALS, 4)
        # avgs["sls"] = round(time_tsp(sls, graph) / NUM_TRIALS, 4)

        # write_times(f, n, avgs)
        print(n, avgs)
