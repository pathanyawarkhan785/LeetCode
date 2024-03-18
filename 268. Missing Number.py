class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for num in range(0, len(nums) + 1):
            if num not in nums:
                temp = num

        return temp


newMissingNumber = Solution()
print(newMissingNumber.missingNumber([3, 0, 1]))
