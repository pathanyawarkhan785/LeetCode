from collections import Counter


class Solution:
    def findDuplicate(self, nums):
        d = Counter(nums)
        duplVal = [key for key, val in d.items() if val > 1]
        return duplVal[0]


newFindDuplicate = Solution()
print(newFindDuplicate.findDuplicate([1, 3, 4, 2, 2]))
