from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr):

        newDict = Counter(arr).values()
        return len(newDict) == len(set(newDict))


newUnique = Solution()
print(newUnique.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
