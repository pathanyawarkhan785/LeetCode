class Solution:
    def findMin(self, nums: list[int]) -> int:

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return nums[start]


newfindMin = Solution()
print(newfindMin.findMin([3, 4, 5, 1, 2]))
