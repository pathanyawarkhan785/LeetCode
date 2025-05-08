class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:

        totalSum = sum(nums)
        left = 0
        count = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            right = totalSum - left

            if left >= right:
                count += 1

        return count


newWay = Solution()
print(newWay.waysToSplitArray([10, 4, -8, 7]))
