import heapq

class my_queue:
    # heap-based priority queue for top items
    def __init__(self):
        self.top_items = []

    def push_item(self, item):
        # minus to make the largest scores the smallest
        heapq.heappush(self.top_items, (item[1], -item[0]))

    def f_top_ten(self):
        top_ten_items = []
        for i in range(3):
            # minus to revert minus in push_item
            large_item = heapq.heappop(self.top_items)
            top_ten_items.append((-large_item[0],large_item[1]))

        print(top_ten_items)

def test_function(matrix):
    matrix[0][0] = 1

if __name__ == '__main__':
    matrix = [[0 for x in range(10)] for x in range(10)]
    test_function(matrix)
    print(matrix[0][0])

