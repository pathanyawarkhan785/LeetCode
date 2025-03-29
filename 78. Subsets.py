class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result


newSubSets = Solution()
print(newSubSets.subsets([3, 2, 4, 1]))
