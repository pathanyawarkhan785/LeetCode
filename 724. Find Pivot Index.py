class Solution:
    def pivotIndex(self, nums):

        leftSum = 0
        rightSum = 0
        lenOfNums = len(nums)
        sumOfNums = sum(nums)

        for i in range(lenOfNums):
            rightSum = sumOfNums - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            i += 1

        return -1


newPivot = Solution()
print(newPivot.pivotIndex([1, 7, 3, 6, 5, 6]))

# 0  1  8  11
# 27 20 17 11
