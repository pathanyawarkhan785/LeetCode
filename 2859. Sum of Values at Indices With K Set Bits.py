class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        count = 0
        res = 0
        for i in range(len(nums)):
            n = i
            while n > 0:
                if n & 1 == 1:
                    count = count + 1
                n = n >> 1
            if count == k:
                res += nums[i]
            count = 0
        return res


newSum = Solution()
newSum.sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1)
