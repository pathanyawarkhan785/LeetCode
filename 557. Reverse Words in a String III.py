class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        for i in range(len(s)):
            s[i] = (s[i])[::-1]

        return " ".join(s)


newReverse = Solution()
print(newReverse.reverseWords("Let's take LeetCode contest"))
