class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if bin(nums[i] | nums[j])[-1] == "0":
                    return True
        return False


newTrailing = Solution()
print(newTrailing.hasTrailingZeros([1, 2, 3, 4, 5]))
