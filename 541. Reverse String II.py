class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        if len(s) < k:
            return s[::-1]

        s = list(s)

        for i in range(0, len(s), 2 * k):
            s[i : i + k] = reversed(s[i : i + k])

        return "".join(s)


newreverse = Solution()
print(newreverse.reverseStr("abcdefg", 2))
