import unittest
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
            top_ten_items.append((large_item[0],-large_item[1]))

        print(top_ten_items)


class Solution:

    '''
    Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

    The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews, sort alphabetically.
    '''
    def problemOne(self):
        heap = my_queue()
        heap.push_item((10, "A"))
        heap.push_item((12, "B"))
        heap.push_item((5, "C"))
        heap.push_item((7, "D"))
        heap.push_item((3, "e"))
        heap.push_item((80, "f"))
        heap.push_item((68, "g"))
        heap.push_item((71, "h"))
        heap.push_item((55, "i"))
        heap.push_item((47, "j"))
        heap.f_top_ten()



# class AMCATTests(unittest.TestCase):
#
#     def test_one_problemOne(self):
#         k = 2
#         keywords = ["anacell", "cetracular", "betacellular"]
#         reviews = [
#             "Anacell provides the best services in the city",
#             "betacellular has awesome services",
#             "Best services provided by anacell, everyone should use anacell",
#         ]
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_two_one_problemOne(self):
#         k = 2
#         keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
#         reviews = [
#             "I love anacell Best services; Best services provided by anacell",
#             "betacellular has great services",
#             "deltacellular provides much better services than betacellular",
#             "cetracular is worse than anacell",
#             "Betacellular is better than deltacellular.",
#         ]
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

if __name__ == '__main__':
    s = Solution()
    s.problemOne()
    # unittest.main()