class Solution:
    def isPalindrome(self, s):
        temp = ""
        specialCharList = [
            ",",
            ":",
            " ",
            ".",
            "@",
            "#",
            "_",
            "{",
            "}",
            "\\",
            '"',
            "[",
            "]",
            "'",
            "-",
            "?",
            ";",
            "!",
            "(",
            ")",
            "`",
        ]
        for i in range(0, len(specialCharList)):
            s = s.replace(specialCharList[i], "").lower()
        temp = s[::-1]
        return True if (s == temp) else False


newIsPalindrome = Solution()
print(
    newIsPalindrome.isPalindrome("Damosel, a poem? A carol? Or a cameo pale? (So mad!)")
)
