import unittest
from mediums.medium_leet import Medium_LC_set1 as Solution_set1

class MediumLCSet1Tests(unittest.TestCase):
    # def test_p1_t1(self):
    #     s = Solution_set1()
    #     self.assertEqual(s.p1(226), 3)
    #
    # def test_p1_t2(self):
    #     s = Solution_set1()
    #     self.assertEqual(s.p1(1201234), 3)
    #
    # def test_p1_t3(self):
    #     s = Solution_set1()
    #     self.assertEqual(s.p1(0), 0)
    #
    # def test_p1_t4(self):
    #     s = Solution_set1()
    #     self.assertEqual(s.p1(1), 1)

    def test_p2_t1(self):
        s = Solution_set1()

        self.assertListEqual(s.p2([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

    def test_p4_t1(self):
        s = Solution_set1()
        self.assertListEqual(s.p4([1,2,3,4]), [24,12,8,6])

    def test_p5_t1(self):
        s = Solution_set1()
        self.assertEqual(s.p5([[0, 30],[5, 10],[15, 20]]), 2)

    def test_p5_t2(self):
        s = Solution_set1()
        self.assertEqual(s.p5([[7,10],[2,4]]), 1)

    def test_p6_t1(self):
        s = Solution_set1()
        self.assertEqual(s.p6("ababcbacadefegdehijhklij"), [9,7,8])

    def test_p6_t2(self):
        s = Solution_set1()
        self.assertEqual(s.p6("eaaaabaaec"), [9,1])

    def test_p6_t3(self):
        s = Solution_set1()
        self.assertEqual(s.p6("caedbdedda"), [1,9])
if __name__ == '__main__':
    unittest.main()