import unittest
from top_hundred_liked.top_hundred_liked_set1 import Solution_THL_LC_set1 as Solution

class TopHundredLCSet1Tests(unittest.TestCase):
    def test_p1_t1(self):
        s = Solution()
        self.assertEqual(3, s.p1("abcabcbb"))

    def test_p1_t2(self):
        s = Solution()
        self.assertEqual(1, s.p1("bbbbb"))

    def test_p1_t3(self):
        s = Solution()
        self.assertEqual(3, s.p1("pwwkew"))

    def test_p1_t4(self):
        s = Solution()
        self.assertEqual(0, s.p1(""))

    def test_p2_t1(self):
        s = Solution()
        self.assertListEqual([24,12,8,6], s.p2([1,2,3,4]))

    def test_p3_t1(self):
        s = Solution()
        nums = [-2,0,-1]
        print(s.p3(nums))
        self.assertEqual(0, s.p3(nums))