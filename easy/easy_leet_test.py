from easy_leet import Solution
import unittest

class EasyLCTests(unittest.TestCase):
    def test_p1_t1(self):
        s = Solution()
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(s.p1(words, order))

    def test_p1_t2(self):
        s = Solution()
        words = ["word","word", "world","row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(s.p1(words, order))

    def test_p1_t3(self):
        s = Solution()
        words = ["apple","app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(s.p1(words, order))

if __name__ == '__main__':
    unittest.main()