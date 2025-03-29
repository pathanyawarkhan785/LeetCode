class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if (mid == 0 or nums[mid] != nums[mid - 1]) and (
                mid == len(nums) - 1 or nums[mid] != nums[mid + 1]
            ):
                return nums[mid]

            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (
                mid % 2 == 0 and nums[mid] == nums[mid + 1]
            ):
                start = mid + 1
            else:
                end = mid - 1

        return nums[start]


newSingle = Solution()
print(newSingle.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
