class Solution:
    def reverseWords(self, s):
        return " ".join(
            reversed([word for word in s.split() if word.isalnum()])
        ).strip()


newRev = Solution()
print(newRev.reverseWords("the sky is blue"))
