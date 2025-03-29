class Solution:
    def countKeyChanges(self, s):
        count = 0
        lenOfS = len(s)
        s = s.lower()

        for i in range(lenOfS):
            if i + 1 < lenOfS and s[i] != s[i + 1]:
                count += 1
        return count


newCount = Solution()
print(newCount.countKeyChanges("mDVD"))
