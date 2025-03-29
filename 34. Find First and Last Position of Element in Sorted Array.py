class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binarySearch(nums, target, search):
            start = 0
            end = len(nums) - 1
            res = []
            ind = -1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] < target:
                    start = mid + 1

                elif nums[mid] > target:
                    end = mid - 1

                else:
                    ind = mid
                    if search:
                        end = mid - 1
                    else:
                        start = mid + 1

            return ind

        leftInd = binarySearch(nums, target, True)
        rightInd = binarySearch(nums, target, False)

        return [leftInd, rightInd]


nums = [5, 7, 7, 8, 8, 10]
target = 8

newSearch = Solution()
print(newSearch.searchRange(nums, target))
