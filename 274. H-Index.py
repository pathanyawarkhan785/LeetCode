class Solution:
    def hIndex(self, citations):
        max = 0
        citations.sort()
        print(citations)
        for i in range(1, len(citations) + 1):
            if citations[i - 1] >= i:
                max = i
            else:
                return max


newHIndex = Solution()
print(newHIndex.hIndex([3, 0, 6, 1, 5]))
