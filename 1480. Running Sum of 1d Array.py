class Solution:
    def runningSum(self, nums):
        newList = []
        for i in range(len(nums)):
            if i + 1 < len(nums):
                sum = nums[i] + nums[i + 1]
                nums[i + 1] = sum

        return nums


newRunningSum = Solution()
print(newRunningSum.runningSum([1, 2, 3, 4]))
