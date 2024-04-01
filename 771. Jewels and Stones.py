class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        temp = 0
        for i in range(0, len(jewels)):
            temp += stones.count(jewels[i])
        return temp


newNumJewels = Solution()
print(newNumJewels.numJewelsInStones("aA", "aAAbbbb"))
