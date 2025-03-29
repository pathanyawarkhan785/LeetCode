class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        count = 0

        while x > 0:
            if x & 1 == 1:
                count += 1
            x = x >> 1

        return count


newhamming = Solution()
print(newhamming.hammingDistance(1, 4))
