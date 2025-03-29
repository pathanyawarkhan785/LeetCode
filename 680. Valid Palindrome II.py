class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                leftPart, rightPart = s[start + 1 : end + 1], s[start:end]
                return leftPart == leftPart[::-1] or rightPart == rightPart[::-1]
            start += 1
            end -= 1

        return True


newValid = Solution()
print(newValid.validPalindrome("racecyar"))
