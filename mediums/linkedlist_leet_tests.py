import unittest
from linkedlist_leet import Solution, SLLNode


def listToLL(arr):
    head = SLLNode(arr[0])

    temp = head
    i = 1

    while i < len(arr):
        temp.next(SLLNode(arr[i]))
        temp = temp.next
        i += 1

    return head


def compareLL(l1, l2):
    temp1 = l1
    temp2 = l2
    while temp1 is not None and temp2 is not None:
        if temp1.val != temp2.val:
            return False
    return True


class LinkedList_leet_medium(unittest.TestCase):
    def test_p1_t1(self):
        s = Solution()
        l1 = [7, 2, 4, 3]
        l1 = listToLL(l1)

        l2 = [5, 6, 4]
        l2 = listToLL(l2)

        l3 = [7, 8, 0, 7]
        l3 = listToLL(l3)

        self.assertTrue(compareLL(s.p1(l1, l2), l3))


if __name__ == '__main__':
    unittest.main()
