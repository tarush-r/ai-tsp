import random
import sys

from structs import *


def generateInitialPath(graph: Graph):
    startNode = 0
    path = [startNode]
    for i in range(1, graph.numNodes):
        path.append(i)
    path.append(startNode)
    return path


def getPathCost(graph: Graph, path: List[Node]):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph.adjMatrix[path[i]][path[i + 1]]
    return cost


def getNeighbors(graph: Graph, currPath: List[Node]):
    n = len(currPath)
    originalPath = list(currPath)
    initialCost = getPathCost(graph, currPath)
    neighbors = []
    for i in range(n - 4):
        for j in range(i + 2, n - 2):
            temp = currPath[i + 1]
            currPath[i + 1] = currPath[j + 1]
            currPath[j + 1] = temp
            if getPathCost(graph, currPath) <= initialCost:
                neighbors.append(list(currPath))

            currPath = list(originalPath)
    return neighbors


def chooseRandomNeighbor(graph: Graph, neighbors: List[List[Node]]):
    weights = [0] * len(neighbors)
    pathCosts = [0] * len(neighbors)
    totalSum = 0
    for i in range(len(neighbors)):
        pathCosts[i] = getPathCost(graph, neighbors[i])
        totalSum += pathCosts[i]

    for i in range(len(neighbors)):
        weights[i] = totalSum // pathCosts[i]

    return random.choices(neighbors, weights=weights, k=1)[0]


def getMinCostOfNeighbors(graph: Graph, neighbors: List[List[Node]]):
    minCost = sys.maxsize
    for path in neighbors:
        minCost = min(minCost, getPathCost(graph, path))
    return minCost


def sls(graph: Graph, maxItr=10000):
    currPath = generateInitialPath(graph)
    while maxItr != 0:
        currPathCost = getPathCost(graph, currPath)
        neighbors = getNeighbors(graph, currPath)
        minNeighborCost = getMinCostOfNeighbors(graph, neighbors)
        if len(neighbors) == 0 or minNeighborCost >= currPathCost:
            break
        currPath = chooseRandomNeighbor(graph, neighbors)
        maxItr -= 1
    minCost = getPathCost(graph, currPath)
    return minCost, currPath
