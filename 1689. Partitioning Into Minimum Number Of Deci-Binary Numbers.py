class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, n))


newMin = Solution()
print(newMin.minPartitions("82734"))
