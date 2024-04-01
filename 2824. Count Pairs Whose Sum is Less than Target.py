class Solution:
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i + 1 < len(nums) and nums[i] + nums[j] < target:
                    count += 1
        return count


newCountPairs = Solution()
print(newCountPairs.countPairs([-1, 1, 2, 3, 1], 2))
