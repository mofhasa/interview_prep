import unittest
from hackerrank.HR_medium import HRMedium_set1 as Solution_s1


class HRMedium_set1_tests(unittest.TestCase):
    def test_p1_t1(self):
        s = Solution_s1()
        self.assertEqual(True, s.p1("()"))
    def test_p1_t2(self):
        s = Solution_s1()
        self.assertEqual(True, s.p1("()[]{}"))
    def test_p1_t3(self):
        s = Solution_s1()
        self.assertEqual(False, s.p1("(]"))
    def test_p1_t4(self):
        s = Solution_s1()
        self.assertEqual(False, s.p1("([)]"))
    def test_p1_t5(self):
        s = Solution_s1()
        self.assertEqual(True, s.p1("{[]}"))
