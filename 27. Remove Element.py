nums = [3, 2, 2, 3]
val = 3


class Solution:
    def removeElement(self, nums, val):
        for i in range(0, len(nums)):
            # method 1


            # if nums[i] == val:
            #     nums.pop(nums[i])

            # method 2

            # if val in nums:
            #     nums.pop(nums[i])
        # return nums


newElem = Solution()
print(newElem.removeElement(nums, val))
