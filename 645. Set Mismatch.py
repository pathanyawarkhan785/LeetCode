class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        num_set = set(nums)
        duplicate = sum(nums) - sum(num_set)
        n = len(nums)
        missing = n * (n + 1) // 2 - sum(num_set)
        return [duplicate, missing]


newFind = Solution()
print(newFind.findErrorNums([1, 2, 2, 4]))
