
def doCharactersRepeat(s):
    if len(list(s)) == len(set(s)): return False
    else: return True


def subArrayMultiplier(sub_arr):
    prod = 1
    for x in sub_arr:
        prod *= x

    return prod

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

    def p3(self, nums):
        i = 0
        j = 0

        max_prod_yet = 0
        while i < len(nums) and j < len(nums):
            print(i,j,max_prod_yet)
            curr_prod = subArrayMultiplier(nums[i:j + 1])
            print(curr_prod)
            if curr_prod >= max_prod_yet:
                max_prod_yet = curr_prod
                j += 1
            elif curr_prod < max_prod_yet:
                if (i != 0 and j != 0) and (i == j):
                    j += 1
                else:
                    i += 1
                    while curr_prod < max_prod_yet:
                        curr_prod = subArrayMultiplier(nums[i:j + 1])
                        print(curr_prod)
                        if i == j:
                            break
                        i += 1
        return max_prod_yet

    def p4(self):
        pass
    def p5(self):
        pass

