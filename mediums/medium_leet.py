from heapq import heappush, heapify, heappop
def prodArr(arr, i):
    prod = 1
    for k,v in enumerate(arr):
        if k != i:
            prod *= v
    return prod

class Medium_LC_set1:
    #Decode Ways
    def p1(self, nums):
        pass

    # Three sum to 0
    def p2(self, nums):
        nums = sorted(nums)
        ret = []
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] > 0:
                break

            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(i, nums, ret)

            i += 1
        return ret

    def twoSum(self, x, nums, ret):
        i = x+1
        j = len(nums) - 1

        while i < j:
            cur_sum = nums[x] + nums[i] + nums[j]
            if cur_sum == 0:
                ret.append([nums[x], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif cur_sum > 0:
                j -= 1
            else:
                i += 1

    # 253. Meeting Rooms II: leetcode.com/problems/meeting-rooms-ii/
    def p3(self):
        pass

    # (238) Product of Array Except self
    def p4(self, arr):
        i = 0
        n = len(arr)
        ret = []
        while i < n:
            ret.append(prodArr(arr,i))
            i += 1

        return ret

    # 253. Meeting Rooms 2
    def p5(self, sched):
        sched.sort(key=lambda x: x[0])
        pq = []
        heapify(pq)

        rooms = 0
        for k,v in enumerate(sched):
            if k == 0:
                heappush(pq, [v[1], v[0]])
                rooms += 1
            else:
                if pq[0][0] <= v[0]:
                    heappop(pq)
                    heappush(pq, [v[1], v[0]])
                else:
                    heappush(pq, [v[1], v[0]])
                    rooms += 1
        return rooms

    #763. Partition Labels
    def p6(self, s):
        occur = {}
        for x in s:
            if x not in occur.keys():
                occur[x] = s.rfind(x)

        start = 0
        end = 0
        ret = []
        for k,v in enumerate(s):
            end = max(end, occur[v])
            if k == end:
               ret.append(k-start+1)
               start = k + 1

        return ret








# class C3_LC_set:
#     pass
