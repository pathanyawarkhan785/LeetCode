class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = 0

        for i in range(len(s) - 2):
            temp = s[i : i + 3]
            if len(temp) == len(set(temp)):
                count += 1

        return count


newCount = Solution()
print(newCount.countGoodSubstrings("xyzzaz"))
