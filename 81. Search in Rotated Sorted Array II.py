class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False


newSearch = Solution()
print(newSearch.search([2, 5, 6, 0, 0, 1, 2], 3))
