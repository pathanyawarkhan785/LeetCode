class Solution:
    def findTheDifference(self, s, t):
        temp = ""
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        for i in range(0, len(s)):
            if t[i] == s[i]:
                t.replace(t[i], "")
        print(t)
        # return temp


newFindDifference = Solution()
print(newFindDifference.findTheDifference("a", "aa"))
