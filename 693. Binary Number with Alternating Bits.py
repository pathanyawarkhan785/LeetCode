class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xor = n ^ (n >> 1)
        return (xor & (xor + 1)) == 0


newHasAlternate = Solution()
print(newHasAlternate.hasAlternatingBits(7))
