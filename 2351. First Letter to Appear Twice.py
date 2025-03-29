class Solution:
    def repeatedCharacter(self, s):

        seen = set()

        for val in s:
            if val in seen:
                return val
            else:
                seen.add(val)


newRepeated = Solution()
print(newRepeated.repeatedCharacter("abccbaacz"))
