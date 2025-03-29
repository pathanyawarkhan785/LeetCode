class Solution:
    def isSubsequence(self, s, t):

        lenOfS = len(s)
        lenOfT = len(t)

        if lenOfS == 0:
            return True

        if lenOfS > lenOfT:
            return False

        j = 0

        for i in range(lenOfT):
            if t[i] == s[j]:
                if j == lenOfS - 1:
                    return True
                j += 1

        return False


newIsSubSequence = Solution()
print(newIsSubSequence.isSubsequence("abc", "ahbgdc"))
