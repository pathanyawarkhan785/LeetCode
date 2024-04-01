class Solution:
    def containsDuplicate(self, nums):
        numSet = list(set(nums))
        numSet.sort()
        nums.sort()
        return False if numSet == nums else True


newContainsDupl = Solution()
print(newContainsDupl.containsDuplicate([1, 2, 3, 1]))
