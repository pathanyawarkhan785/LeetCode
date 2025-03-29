from collections import defaultdict


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:

        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        max_freq = max(frequency.values())
        result = [[] for _ in range(max_freq)]

        for num, count in frequency.items():
            for i in range(count):
                result[i].append(num)

        return result


newFind = Solution()
print(newFind.findMatrix([1, 3, 4, 1, 2, 3, 1]))
