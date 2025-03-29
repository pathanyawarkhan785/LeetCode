class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return int((len(nums) + 1) * len(nums) / 2 - sum(nums))


newMissingNumber = Solution()
print(newMissingNumber.missingNumber([3, 0, 1]))
