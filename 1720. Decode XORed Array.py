class Solution(object):
    def decode(self, encoded, first):
        # print(encoded, first)
        realList = [first]
        for i in range(len(encoded)):
            realList.append(encoded[i] ^ realList[i])
        return realList


newDecode = Solution()
print(newDecode.decode([1, 2, 3], 1))
