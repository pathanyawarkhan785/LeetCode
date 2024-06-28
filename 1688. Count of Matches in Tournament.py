class Solution(object):
    def numberOfMatches(self, n):
        count = 0
        while 1:
            if n == 1:
                return count
            if n % 2:
                matches = (n - 1) / 2
                advance = matches + 1
                count += matches
                n = advance
            else:
                matches = n / 2
                advance = n / 2
                count += matches
                n = advance


newNumberOfMatches = Solution()
print(newNumberOfMatches.numberOfMatches(14))
