class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]

        firstOne = -1
        maxDist = 0

        for i, bit in enumerate(n):
            if bit == "1":
                if firstOne != -1:
                    maxDist = max(maxDist, i - firstOne)
                firstOne = i

        return maxDist


newBinary = Solution()
print(newBinary.binaryGap(22))
