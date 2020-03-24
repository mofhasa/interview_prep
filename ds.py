# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Graph with nodes elements embedded numerical value from 0 to v
class Graph:
    def __init__(self, v, edges=None):
        self.v = v
        self.e = 0
        self.adj_mat = [[0 for x in range(v)] for y in range(v)]
        self.initializeEdges(edges)

    def initializeEdges(self, edges):
        if edges is None:
            while 1:
                e = input()
                if len(e) != 0:
                    e = e.split(",")
                    src = int(e[0])
                    dest = int(e[1])
                    self.adj_mat[src][dest] = 1
                    self.e += 1
                else:
                    break
        else:
            for ee in edges:
                self.adj_mat[ee[0]][ee[1]] = 1
                self.e += 1

    