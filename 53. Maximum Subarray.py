class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        maxSum = float("-inf")
        currSum = 0
        lenOFNums = len(nums)

        for i in range(lenOFNums):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0

        return maxSum


newMaxSub = Solution()
print(newMaxSub.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
