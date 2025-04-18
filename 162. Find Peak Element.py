class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1

        return start


newFind = Solution()
print(newFind.findPeakElement([1, 2, 3, 1]))
