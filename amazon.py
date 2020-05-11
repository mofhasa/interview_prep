import unittest
# from ds import MinStack
import heapq

import math

def safeMoves(i, k, stones, stones_map):
    moves = []

    if k - 1 > 0 and stones[i] + (k - 1) in stones:
        moves.append((stones_map[stones[i] + (k - 1)], k - 1))

    if k > 0 and stones[i] + k in stones:
        moves.append((stones_map[stones[i] + k], k))

    if k + 1 > 0 and stones[i] + (k + 1) in stones:
        moves.append((stones_map[stones[i] + (k + 1)], k + 1))

    return moves


def dfsUtil(i, k, visited, stones, stones_index_map):
    visited[i] = True

    for xyz in safeMoves(i, k, stones, stones_index_map):
        dfsUtil(xyz[0], xyz[1], visited, stones, stones_index_map)


def getGreaterNumber(index, nums):
    # if len(ret) > 0:
    #     if nums[index-1] >= nums[index]:
    #         return ret[index-1]

    len_max = len(nums)
    i = (index + 1) % len_max
    max_yet = -1
    if i < (index + 1):
        while i != index:
            if nums[i] > nums[index]:
                max_yet = nums[i]
                return max_yet
            i += 1
    else:
        while i < len_max:
            if nums[i] > nums[index]:
                max_yet = nums[i]
                return max_yet
            i += 1
        i = (i) % len(nums)
        while i != index:
            if nums[i] > nums[index]:
                max_yet = nums[i]
                return max_yet
            i += 1
    return max_yet


class Solution:
    '''
        We are given some website visits: the user with name username[i] visited the website website[i] at time
        timestamp[i].

        A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
        (The websites in a 3-sequence are not necessarily distinct.)

        Find the 3-sequence visited by the largest number of users. If there is more than one solution,
        return the lexicographically smallest such 3-sequence.
    '''
    def p1(self):
        pass


    '''
    Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

    Follow up:
    Could you solve it in linear time?
    '''
    def p2(self):

        return [3, 3, 5, 5, 6, 7]


    '''
        
    '''
    def p3(self, paragraph, banned):
        def isAlphabet(c):
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                return True
            else:
                return False

        all_words = paragraph.split(" ")
        final_words = []

        for word in all_words:
            if len(word.split(",")) > 1:
                word = word.split(",")
                for w in word:
                    if len(w) > 0:
                        final_words.append(w)
            elif len(word) > 0:
                final_words.append(word)

        freq_table = {}
        for word in final_words:
            word = word.lower()

            if not isAlphabet(word[-1]):
                word = word[0:-1]


            if word in freq_table.keys():
                freq_table[word] += 1
            else:
                freq_table[word] = 1

        myheap = []

        for k in freq_table.keys():
            heapq.heappush(myheap, (-freq_table[k], k))

        while True:
            curr_word = heapq.heappop(myheap)
            if curr_word[1] not in banned:
                return curr_word[1]

    def p4(self, nums):
            i = 0
            ret = []
            while i < len(nums):
                ret.append(getGreaterNumber(i, nums))
                i += 1

            return ret


    def p5(self, stones):
        num_stones = len(stones)
        visited = [False] * num_stones
        stones_index_map = {}

        for i in range(0, num_stones):
            stones_index_map[stones[i]] = i

        k = 1
        i = 1

        dfsUtil(i, k, visited, stones, stones_index_map)
        return visited[num_stones - 1]

    def p6(self, ):

class AmazonLPTests(unittest.TestCase):
    # def test_p1_t1(self):
    #     self.assertEqual(1,1)
    #
    # def test_p2_t1(self):
    #     nums = [1,3,-1,-3,5,3,6,7]
    #     k= 3
    #
    #
    #     solution = Solution()
    #     result = solution.p2(nums, k)
    #
    #     self.assertListEqual(result, [3,3,5,5,6,7])

    # def test_p3_t1(self):
    #     paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
    #     banned =["hit"]
    #
    #     solution = Solution()
    #     result = solution.p3(paragraph, banned)
    #
    #     self.assertEqual(result, "ball")
    #
    # def test_p3_t2(self):
    #     paragraph = "Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. "
    #
    #     banned = ["hit"]
    #
    #     solution = Solution()
    #     result = solution.p3(paragraph, banned)
    #
    #     self.assertEqual(result, "ball")
    #
    # def test_p4_t1(self):
    #     nums = [5,4,3,2,1]
    #     solution = Solution()
    #     result = solution.p4(nums)
    #
    #     self.assertListEqual(result, [-1,5,5,5,5])

    def test_p5_t1(self):
        stones = [0,1,3,5,6,8,12,17]

        solution = Solution()
        result = solution.p5(stones)

        self.assertEqual(True, result)

    def test_p5_t2(self):
        stones = [0,1,2,3,4,8,9,11]

        solution = Solution()
        result = solution.p5(stones)

        self.assertEqual(False, result)





