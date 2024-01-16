from structs import *


def calcHeuristic(graph: Graph, path: List[Node]):
    return (graph.numNodes - len(path)) * graph.minEdgeLength


def branchAndBound(graph: Graph):
    startNode = 0
    minCost = float("inf")
    minPath = None

    def branchAndBoundRec(fromNode, path, costSoFar):
        nonlocal startNode, minCost, minPath

        if len(path) == graph.numNodes:
            # Cycling back to `startNode`
            path.append(startNode)
            costSoFar += graph.adjMatrix[fromNode][startNode]

            if costSoFar < minCost:
                minCost, minPath = costSoFar, path
            return

        if costSoFar + calcHeuristic(graph, path) >= minCost:
            # Don't go down this path
            return

        nbrs = graph.findNbrs(fromNode)
        for toNode in nbrs:
            if toNode not in path:
                branchAndBoundRec(
                    toNode,
                    path + [toNode],
                    costSoFar + graph.adjMatrix[fromNode][toNode],
                )

    branchAndBoundRec(startNode, [startNode], 0)
    return minCost, minPath
