import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Graph with nodes elements embedded numerical value from 0 to v
class Graph_und:
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
                    self.adj_mat[dest][src] = 1
                    self.e += 1
                else:
                    break
        else:
            for ee in edges:
                self.adj_mat[ee[0]][ee[1]] = 1
                self.adj_mat[ee[1]][ee[0]] = 1
                self.e += 1


#Heap

class TupleMaxHeapQueue:
    def __init__(self):
        self.top_items = []

    def push_item(self, item):
        heapq.heappush(self.top_items, (-item[1], item[0]))

    def f_k_ten(self, k):
        top_k_items = []
        for i in range(k):
            large_item = heapq.heappop(self.top_items)
            top_k_items.append((-large_item[0], large_item[1]))
        return top_k_items

    