class Solution:
    def removeElement(self, nums, val):
        temp = []
        for i in range(0, len(nums)):
            # print(nums[i])
            if nums[i] == val:
                nums[i] = nums[i + 1]
                nums.pop(i + 1)
        print(nums)


newRemoveElem = Solution()
print(newRemoveElem.removeElement([0, 1, 2, 3, 0, 4, 2], 2))
