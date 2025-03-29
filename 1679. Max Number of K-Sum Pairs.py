class Solution:
    def maxOperations(self, nums, k):
        lenOfNums = len(nums)
        left = 0
        right = lenOfNums - 1
        count = 0

        nums.sort()

        # print(nums)

        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1

        # print(nums, k, count)
        return count


newMax = Solution()
print(newMax.maxOperations([3, 2, 1, 5, 4], 5))
