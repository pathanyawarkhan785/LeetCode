class Solution:
    def repeatedCharacter(self, s):
        uniqChar = []
        for val in s:
            if val in uniqChar:
                return val
            else:
                uniqChar.append(val)


newRepeated = Solution()
print(newRepeated.repeatedCharacter("abccbaacz"))
