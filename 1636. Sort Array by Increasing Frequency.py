from collections import Counter


class Solution:
    def frequencySort(self, nums):

        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))


newFrequecySort = Solution()
print(newFrequecySort.frequencySort([1, 1, 2, 2, 2, 3]))
