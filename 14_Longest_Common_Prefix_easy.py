class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        for i in range(1, len(strs)):
            temp = ""
            if len(strs[0]) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(strs[0]) and strs[0][j] == strs[i][j]:
                    temp += strs[0][j]
                else:
                    break
            strs[0] = temp
        return strs[0]


newLongestCommon = Solution()
print(newLongestCommon.longestCommonPrefix(["school", "schedule", "scotland"]))
