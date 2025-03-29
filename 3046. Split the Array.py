from collections import Counter


class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        nums = Counter(nums)

        for occur in nums.values():
            if occur > 2:
                return False

        return True


newIsPossible = Solution()
newIsPossible.isPossibleToSplit([1, 1, 2, 2, 3, 4])
