
def doCharactersRepeat(s):
    if len(list(s)) == len(set(s)): return False
    else: return True

class Solution_THL_LC_set1:
    #https://leetcode.com/problems/longest-substring-without-repeating-characters/
    def p1(self, s):
        i = 0
        j = 0
        longestYet = 0

        while i <= j and j < len(s):
            temp = s[i:j+1]

            if not doCharactersRepeat(temp):
                if len(temp) > longestYet:
                    longestYet = len(temp)
                j+=1
            else:
                while doCharactersRepeat(temp):
                    i+=1
                    temp = s[i: j+1]
        return longestYet

    #https://leetcode.com/problems/product-of-array-except-self/
    def p2(self, nums):
        product = 1
        for x in nums:
            product *= x

        ret = []
        for x in nums:
            ret.append(product/x)

        return ret

    def p3(self):
        pass
    def p4(self):
        pass
    def p5(self):
        pass


# class Solution:
#     def p1(self):
#         pass
#     def p2(self):
#         pass
#     def p3(self):
#         pass
#     def p4(self):
#         pass
#     def p5(self):
#         pass