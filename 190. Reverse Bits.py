class Solution:
    def reverseBits(self, n: int) -> int:

        for i in range(16):
            if n >> i & 1 != n >> 32 - i - 1 & 1:
                n = 1 << i ^ n
                n = 1 << (32 - i - 1) ^ n
        return n


newreverse = Solution()
print(newreverse.reverseBits(43261596))
