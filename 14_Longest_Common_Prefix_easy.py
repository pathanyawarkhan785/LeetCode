class Solution:
    def longestCommonPrefix(self, strs):

        strs.sort(key=len)
        temp = strs[0]
        newTemp = ""

        print(strs)

        for i in range(1, len(strs)):
            # print(i, len(strs))
            for j in range(0, len(temp)):
                if temp[j] == strs[i][j]:
                    newTemp += temp[j]

            temp = ""
            temp = newTemp
            newTemp = ""

        return temp


newLongestCommon = Solution()
print(newLongestCommon.longestCommonPrefix(["cir", "car"]))
