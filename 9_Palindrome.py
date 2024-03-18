class Solution:

    def isPalindrome(self, val):
        revInt = str(val)
        if revInt.isnumeric():
            revInt = int(revInt[::-1])
            return True if (val == revInt) else False
        else:
            return False


checkPalindrome = Solution()

print(checkPalindrome.isPalindrome(-121))


# string split , string reverse , string join
