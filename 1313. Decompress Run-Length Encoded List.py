class Solution(object):
    def decompressRLElist(self, nums):
        newNums = []

        i = 0
        while i < len(nums) - 1:
            newNums.append([nums[i + 1]] * nums[i])
            i = i + 2

        newNums = sum(newNums, [])
        return newNums


newDecompress = Solution()
print(newDecompress.decompressRLElist([1, 2, 3, 4]))

# 2, 4, 4, 4
