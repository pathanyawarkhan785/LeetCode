class Solution:
    def smallerNumbersThanCurrent(self, nums):
        newList = []
        count = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            newList.append(count)
            count = 0
        return newList


newSmaller = Solution()
print(newSmaller.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
