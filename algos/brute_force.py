from structs import *


def bruteForce(graph: Graph):
    startNode = 0
    minCost = float("inf")
    minPath = None

    def bruteForceRec(fromNode, path, costSoFar):
        nonlocal startNode, minCost, minPath

        if len(path) == graph.numNodes:
            # Cycling back to `startNode`
            path.append(startNode)
            costSoFar += graph.adjMatrix[fromNode][startNode]

            if costSoFar < minCost:
                minCost, minPath = costSoFar, path
            return

        nbrs = graph.findNbrs(fromNode)
        for toNode in nbrs:
            if toNode not in path:
                bruteForceRec(
                    toNode,
                    path + [toNode],
                    costSoFar + graph.adjMatrix[fromNode][toNode],
                )

    bruteForceRec(startNode, [startNode], 0)
    return minCost, minPath
