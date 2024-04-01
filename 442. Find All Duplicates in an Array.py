from collections import Counter


class Solution:
    def findDuplicates(self, nums):
        temp = []
        d = dict(Counter(nums))
        temp = [key for (key, val) in d.items() if val > 1]
        temp.sort()
        return temp


newFindDuplicate = Solution()
print(newFindDuplicate.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
