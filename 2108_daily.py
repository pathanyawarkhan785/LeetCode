class Solution:
    def firstPalindrome(self, words):

        for val in words:
            if val == val[::-1]:
                return val
        else:
            return ""


newDaily = Solution()
print(newDaily.firstPalindrome(["notapalindrome", "racecar"]))
