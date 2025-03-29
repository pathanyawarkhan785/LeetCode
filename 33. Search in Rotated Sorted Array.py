class Solution:
    def search(self, nums: list[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


newSearch = Solution()
print(newSearch.search([4, 5, 6, 7, 0, 1, 2], 0))
