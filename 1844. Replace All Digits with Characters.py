class Solution:
    def replaceDigits(self, s):

        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = chr(ord(s[i - 1]) + int(s[i]))
        return "".join(s)


newReplaceDigits = Solution()
print(newReplaceDigits.replaceDigits("a1c1e1"))
