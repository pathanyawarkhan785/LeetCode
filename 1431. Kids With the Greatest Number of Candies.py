class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        lst = [
            True if (candies[i] + extraCandies) >= max(candies) else False
            for i in range(0, len(candies))
        ]
        return lst


newKidsWithCandies = Solution()
print(newKidsWithCandies.kidsWithCandies([2, 3, 5, 1, 3], 3))
