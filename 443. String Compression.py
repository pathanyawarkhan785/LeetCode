from collections import Counter


class Solution:
    def compress(self, chars):
        newDict = dict(Counter(chars))
        newStr = ""
        for key in newDict.keys():
            newStr += key
            newStr += str(newDict[key])
        return len(newStr)


newCompress = Solution()
print(newCompress.compress(["a", "a", "b", "b", "c", "c", "c"]))
