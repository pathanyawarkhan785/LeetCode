class Solution:
    def findMaxLength(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if i == nums[i]:
                count += 1