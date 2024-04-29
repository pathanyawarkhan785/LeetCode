class Solution:
    def maxFrequencyElements(self, nums):
        uniqueNums = set(nums)
        uniqueNums = list(uniqueNums)
        i = 0
        valFreq = []
        while i < len(uniqueNums):
            valFreq.append(nums.count(uniqueNums[i]))
            i = i + 1
        temp = valFreq.count(max(valFreq))

        return temp * max(valFreq)


newMaxFrequencyElements = Solution()
newMaxFrequencyElements.maxFrequencyElements([1, 2, 2, 3, 1, 4])
