class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1

        if nums[start] <= nums[end]:
            return nums[start]

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1

        return nums[start]


newFind = Solution()
print(newFind.findMin([2, 2, 2, 0, 1]))
