class Solution:
    def findMaxLength(self, nums):
        nums = list(set(nums))
        nums.sort()
        # print(nums)

        count = 0
        for i in range(len(nums)):
            # print(i, nums[i])
            if i == nums[i]:
                count += 1
        return count


newFindMaxLength = Solution()
print(newFindMaxLength.findMaxLength([0, 1, 0]))
