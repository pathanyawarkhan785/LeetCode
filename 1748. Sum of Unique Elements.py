from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:

        nums = Counter(nums)
        sum = 0

        for i, j in zip(nums.keys(), nums.values()):
            if j == 1:
                sum += i

        return sum


newSum = Solution()
print(newSum.sumOfUnique([1, 2, 3, 2]))
