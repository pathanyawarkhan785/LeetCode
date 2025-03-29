class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:

        if len(nums) == 1:
            return True

        for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) % 2 == 0:
                return False

        return True


newIsArray = Solution()
print(newIsArray.isArraySpecial([4, 3, 1, 6]))
