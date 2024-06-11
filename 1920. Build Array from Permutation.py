class Solution:
    def buildArray(self, nums):
        temp = []
        for i in range(len(nums)):
            temp.append(nums[nums[i]])

        return temp


newBuildArr = Solution()
print(newBuildArr.buildArray([0, 2, 1, 5, 3, 4]))
