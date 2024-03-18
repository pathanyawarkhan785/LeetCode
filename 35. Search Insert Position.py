class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        for i in range(0, len(nums)):
            if nums[i] > target:
                return i
        return len(nums)


insPos = Solution()
print(insPos.searchInsert([1, 3, 5, 6], 2))
