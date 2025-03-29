class Solution:
    def longestOnes(self, nums, k):
        l = 0
        lenOfNums = len(nums)

        for r in range(lenOfNums):
            if nums[r] == 0:
                k -= 1

            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l + 1


newLongest = Solution()
print(newLongest.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
