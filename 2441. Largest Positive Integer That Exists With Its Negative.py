class Solution:
    def findMaxK(self, nums):
        while 1:
            if len(nums) == 0:
                return -1
            maxVal = max(nums)
            if -maxVal in nums:
                return maxVal
            else:
                nums.remove(maxVal)


newFindMax = Solution()
print(newFindMax.findMaxK([-1, 10, 6, 7, -7, 1]))
