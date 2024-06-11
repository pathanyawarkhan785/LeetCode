from itertools import permutations


class Solution:
    def permute(self, nums):
        newNum = permutations(nums)
        newList = []
        for val in list(newNum):
            newList.append((list(val)))
        return newList


newPermute = Solution()
print(newPermute.permute([1, 2, 3]))
