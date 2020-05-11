import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Graph (undirected) with nodes elements embedded numerical value from 0 to v
class Graph_undirected:
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

#Graph (directed) with nodes elements embedded numerical value from 0 to v
class Graph_directed:
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

'''
singly linked list node
'''
class LinkedList:
    def __init__(self, l_arr):
        self.head = ListNode(l_arr[0])
        temp = self.head


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

'''
problem 155 leetcode

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        push(x) -- Push element x onto stack.
        pop() -- Removes the element on top of the stack.
        top() -- Get the top element.
        getMin() -- Retrieve the minimum element in the stack.
'''
class MinStack:
    def __init__(self):
        self.min_stack = []
        self.data = []

    def push(self, x):
        if len(self.data) > 0:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)

        self.data.append(x)

    def pop(self):
        self.min_stack.pop()
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.min_stack[-1]




class Trie:
    pass

class SegmentTree:
    pass

class RangeQuey:
    pass


