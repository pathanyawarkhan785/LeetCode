class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        count = 0
        n = len(nums)

        for i in range(1 << n):
            current_or = 0
            for j in range(n):
                if i & (1 << j):
                    current_or |= nums[j]
            if current_or == max_or:
                count += 1

        return count


newCount = Solution()
print(newCount.countMaxOrSubsets([3, 1]))
