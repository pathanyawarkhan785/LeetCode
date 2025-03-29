from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = Counter(nums)
        return [item for item, _ in count.most_common(k)]


newTopK = Solution()
print(newTopK.topKFrequent([1, 1, 1, 2, 2, 3], 2))
