from typing import List

Node = int

class Graph:
    def __init__(self, adjMatrix: List[List[Node]]):
        self.adjMatrix = adjMatrix
        self.numNodes = len(self.adjMatrix)

        self.cleanupAdjMatrix()

        self.minEdgeLength = self.findMinEdgeLength()

    def cleanupAdjMatrix(self):
        """Replaces edges of length 0 with length infinity."""

        for row in range(self.numNodes):
            for col in range(self.numNodes):
                if self.adjMatrix[row][col] == 0:
                    self.adjMatrix[row][col] = float("inf")

    def findNbrs(self, node: Node):
        nbrs = []
        for toNode in range(self.numNodes):
            if toNode != node and self.adjMatrix[node][toNode] != float("inf"):
                nbrs.append(toNode)
        return nbrs

    def findMinEdgeLength(self):
        return min(min(self.adjMatrix))
