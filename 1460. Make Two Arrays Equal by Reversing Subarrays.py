from collections import Counter


class Solution:
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        if target != arr:
            return False
        return True


newCanBeEqual = Solution()
print(newCanBeEqual.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
