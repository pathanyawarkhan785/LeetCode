class Solution:
    def maxVowels(self, s, k):

        lenOfS = len(s)
        vowels = "aeiou"
        maxVowels = 0
        curVowels = 0

        for i in range(k):
            if s[i] in vowels:
                curVowels += 1

        maxVowels = curVowels

        for i in range(k, lenOfS):

            if s[i - k] in vowels:
                curVowels -= 1

            if s[i] in vowels:
                curVowels += 1

            if curVowels > maxVowels:
                maxVowels = curVowels

            if maxVowels == k:
                return maxVowels

        return maxVowels


newMax = Solution()
print(newMax.maxVowels("abciiidef", 3))
