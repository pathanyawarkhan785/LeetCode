class Solution:
    def firstMissingPositive(self, nums):
        if max(nums) < 1:
            return 1
        nums = set(nums)
        for i in range(1, max(nums) + 1):
            if i not in nums:
                return i
        return max(nums) + 1


newFirstMissing = Solution()
print(newFirstMissing.firstMissingPositive([1,2,0]))
