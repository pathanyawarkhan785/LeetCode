class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        for i in range(len(s) - 2):
            temp = s[i : i + 3]
            print(temp)


newCount = Solution()
newCount.countGoodSubstrings("xyzzaz")
