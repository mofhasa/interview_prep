import unittest

class Solution():

    '''
        Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

        As a reminder, a binary search tree is a tree that satisfies these constraints:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.
    '''
    def problemOne(self):
        pass

    '''
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.
    '''
    def problemTwo(self, nums, target):

        pass

class TestStringMethods(unittest.TestCase):

    def __init__(self):
        super()
        self.solution = Solution()

    def test_problemTwo_1(self):
        nums = [2, 7, 11, 15]
        target = 9

        l_tst = self.solution.problemTwo(nums, target)
        self.assertListEqual([1,2], l_tst)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()