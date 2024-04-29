import math


class Solution:
    def scoreOfString(self, s):
        temp = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                temp += abs((ord(s[i]) - ord(s[i + 1])))
        return temp


newScoreOfString = Solution()
newScoreOfString.scoreOfString("hello")
