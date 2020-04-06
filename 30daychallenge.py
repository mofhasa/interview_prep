import unittest


def p2_sum_of_digits(num):
    num = str(num)
    num = num.split('')
    sum = 0
    for d in num:
        sum = int(d)**2
    return sum


class Week1Solution:
    def p1(self, nums):
        c_set = set()
        for n in nums:
            if n in c_set:
                c_set.remove(n)
            else:
                c_set.add(n)
        return c_set.pop()
    def p2(self, n):
        pass



class Week2solution:
    pass


class ThirtyDayChallengeTests(unittest.TestCase):
    def test_week1_p1_one(self):
        nums = [2,2,1]
        solution = Week1Solution()
        result = solution.p1(nums)
        test = 1
        self.assertEqual(test, result)

    def test_week1_p1_two(self):
        nums = [4,1,2,1,2]
        solution = Week1Solution()
        result = solution.p1(nums)
        test = 4
        self.assertEqual(test, result)

    def test_week1_p2_one(self):
        pass