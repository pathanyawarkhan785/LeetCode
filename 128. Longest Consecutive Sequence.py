class Solution:
    def longestConsecutive(self, nums):
        setNums = set(nums)
        longest = 0

        for num in setNums:
            if num - 1 not in setNums:
                length = 1
                while num + length in setNums:
                    length += 1
                longest = max(longest, length)

        return longest


newLongestCons = Solution()
print(newLongestCons.longestConsecutive([100, 4, 200, 1, 3, 2]))
