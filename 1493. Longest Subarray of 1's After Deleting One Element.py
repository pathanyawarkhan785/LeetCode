class Solution:
    def longestSubarray(self, nums):
        l = 0
        lenOfNums = len(nums)
        maxWindow = 0
        countOfZero = 0

        for r in range(lenOfNums):
            if nums[r] == 0:
                countOfZero += 1

            while countOfZero > 1:
                if nums[l] == 0:
                    countOfZero -= 1
                l += 1

            currWindow = r - l + 1
            maxWindow = max(currWindow, maxWindow)

        return maxWindow - 1


newLongest = Solution()
print(newLongest.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
