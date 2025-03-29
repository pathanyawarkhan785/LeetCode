from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count = 0
        newNums = []

        countNums = Counter(nums)

        for i, j in countNums.items():
            if j > n / 3:
                newNums.append(i)

        return newNums


newMajority = Solution()
print(newMajority.majorityElement([3, 2, 3]))
