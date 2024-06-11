class Solution:
    def isSubsequence(self, s, t):
        for i in range(len(t)):
            if t[i] not in s:
                return True

        return False


newIsSubSequence = Solution()
print(newIsSubSequence.isSubsequence("axc", "ahbgdc"))
