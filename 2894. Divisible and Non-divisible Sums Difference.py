class Solution:
    def differenceOfSums(self, n, m):
        lst = sum([i for i in range(1, n + 1) if i % m != 0])
        lst2 = sum([i for i in range(1, n + 1) if i % m == 0])
        return lst - lst2


newDifference = Solution()
print(newDifference.differenceOfSums(10, 3))
