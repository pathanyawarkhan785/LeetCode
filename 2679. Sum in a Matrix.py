class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        for row in nums:
            row.sort()
        return sum(map(max, zip(*nums)))


newMatrix = Solution()
print(newMatrix.matrixSum([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]))
