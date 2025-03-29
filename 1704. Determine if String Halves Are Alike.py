class Solution:
    def halvesAreAlike(self, s):

        halfStr = len(s) // 2
        vowelsStr = "aeiouAEIOU"
        count = 0

        for i in range(halfStr):
            if s[i] in vowelsStr:
                count += 1
            if s[i + halfStr] in vowelsStr:
                count -= 1

        return count == 0


newHalves = Solution()
print(newHalves.halvesAreAlike("book"))
