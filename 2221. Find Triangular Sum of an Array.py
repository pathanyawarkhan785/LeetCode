class Solution(object):
    def triangularSum(self, nums):
        newNums = []
        for i in range(len(nums)):
            if i <= 3:
                newNums.append(nums[i] + nums[i + 1])
                # nums.remove(nums[i])
        print(newNums)


newTriangle = Solution()
newTriangle.triangularSum([1, 2, 3, 4, 5])
