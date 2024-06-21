class Solution:
    def isAcronym(self, words, s):

        if len(words) != len(s):
            return False

        for i in range(len(s)):
            if words[i][0] != s[i]:
                return False
        return True


newIsAcronym = Solution()
print(newIsAcronym.isAcronym(["never", "gonna", "give", "up", "on", "you"], "ngguoy"))
