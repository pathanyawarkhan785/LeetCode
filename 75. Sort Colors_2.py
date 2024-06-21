class Solution:
    def sortColors(self, nums):
        newNums = []
        while nums:
            minVal = nums[0]
            for elem in nums:
                if elem < minVal:
                    minVal = elem

            nums.remove(minVal)
            newNums.append(minVal)

        return newNums


newSort = Solution()
print(newSort.sortColors([2, 0, 2, 1, 1, 0]))
