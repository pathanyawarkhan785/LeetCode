class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        newStr = word.split(ch, 1)
        return ch + newStr[0][::-1] + newStr[1]


newReverse = Solution()
print(newReverse.reversePrefix("abcdefd", "d"))
