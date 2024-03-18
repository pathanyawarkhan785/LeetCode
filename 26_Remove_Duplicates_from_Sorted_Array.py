class Solution:
    def removeDuplicates(self, nums):

        nums = set(nums)
        print(list(nums))
        return len(nums)


newVal = Solution()
print(newVal.removeDuplicates([1, 2, 3]))
