class Solution:
    def maxFrequencyElements(self, nums):
        uniqueNums = set(nums)
        uniqueNums = list(uniqueNums)
        # print(uniqueNums)
        i = 0
        valFreq = []
        while i < len(uniqueNums):
            valFreq.append(nums.count(uniqueNums[i]))
            i = i + 1
        print(valFreq)
        temp = valFreq.count(max(valFreq))
        print(temp)

