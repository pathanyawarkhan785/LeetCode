class Solution:
    def sumBase(self, n: int, k: int) -> int:

        temp = 0

        while n:
            temp += n % k
            n = n // k

        return temp


newSum = Solution()
print(newSum.sumBase(34, 6))
