class Solution:
    def findMaxAverage(self, nums, k):

        maxSum = currSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum = currSum - nums[i - k] + nums[i]
            if currSum > maxSum:
                maxSum = currSum

        return maxSum / k


newFindMax = Solution()
print(newFindMax.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
