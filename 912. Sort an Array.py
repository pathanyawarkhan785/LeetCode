class Solution:
    def sortArray(self, nums):

        if len(nums) > 1:

            mid = len(nums) // 2
            leftArr = nums[:mid]
            rightArr = nums[mid:]

            self.sortArray(leftArr)
            self.sortArray(rightArr)

            i = 0
            j = 0
            k = 0

            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] < rightArr[j]:
                    nums[k] = leftArr[i]
                    i += 1
                else:
                    nums[k] = rightArr[j]
                    j += 1
                k += 1

            while i < len(leftArr):
                nums[k] = leftArr[i]
                i += 1
                k += 1

            while j < len(rightArr):
                nums[k] = rightArr[j]
                j += 1
                k += 1
        return nums


newSort = Solution()
print(newSort.sortArray([5, 2, 3, 1]))
