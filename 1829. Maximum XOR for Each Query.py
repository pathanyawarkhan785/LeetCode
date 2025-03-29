class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        maxXor = (1 << maximumBit) - 1
        xorAll = 0

        for num in nums:
            xorAll ^= num

        result = []

        for i in range(len(nums) - 1, -1, -1):
            result.append(xorAll ^ maxXor)
            xorAll ^= nums[i]

        return result


newMax = Solution()
print(newMax.getMaximumXor([0, 1, 1, 3], 2))
