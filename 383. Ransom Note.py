from collections import Counter


class Solution:
    def canConstruct(self, ransomNote, magazine):

        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)

        for i, j in ransomNote.items():
            if j > magazine[i]:
                return False

        return True


newConstruct = Solution()
print(newConstruct.canConstruct("aa", "ab"))
