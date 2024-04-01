class Solution:
    def smallestEvenMultiple(self, n):
        while n % 2 != 0:
            n = n * 2
        if n % 2 == 0:
            return n


newSmallest = Solution()
print(newSmallest.smallestEvenMultiple(5))
