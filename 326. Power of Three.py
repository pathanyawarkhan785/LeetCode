class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        elif n == 1:
            return True
        # print(n)
        for i in range(1, 20):
            # print(n)
            # print(n / 3**i == 1, n / 3**i >= 1)
            if n / 3**i == 1 and n / 3**i >= 1:
                return True
        return False


newIsPowerOfThree = Solution()
print(newIsPowerOfThree.isPowerOfThree(27))
