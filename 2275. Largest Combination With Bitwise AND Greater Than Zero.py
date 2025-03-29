class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        maxCount = 0

        for i in range(24):
            count = sum((num >> i) & 1 for num in candidates)
            maxCount = max(maxCount, count)

        return maxCount


newLargest = Solution()
print(newLargest.largestCombination([16, 17, 71, 62, 12, 24, 14]))
