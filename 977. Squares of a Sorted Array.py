class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        # sqNums = []

        # for val in nums:
        #     sqNums.append(val * val)

        # sqNums.sort()
        # return sqNums

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        index = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return result


newSorted = Solution()
print(newSorted.sortedSquares([-4, -1, 0, 3, 10]))
