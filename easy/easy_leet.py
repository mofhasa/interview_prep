from functools import cmp_to_key
class Solution:
    #953. Verifying an Alien Dictionary
    def p1(self, words, order):
        idx_dict = {}
        for x,y in enumerate(words):
            if y in idx_dict.keys():
                idx_dict[y].append(x)
            else:
                idx_dict[y] = [x]

        print(words)
        print(idx_dict)

        order_dict = {}
        for x,y in enumerate(order):
            order_dict[y] = x

        def comparator(a, b):
            i = 0
            j = 0
            n = len(a)
            m = len(b)

            while i < n and j < m:
                if order_dict[a[i]] == order_dict[b[j]]:
                    i += 1
                    j += 1
                elif order_dict[a[i]] < order_dict[b[j]]:
                    return -1
                else:
                    return 1

            if n == m:
                return 0
            elif n < m:
                return -1
            else:
                return 1

        words = sorted(words, key=cmp_to_key(comparator))
        print(words)

        for x,y in enumerate(words):
            if x not in idx_dict[y]:
                return False

        return True


