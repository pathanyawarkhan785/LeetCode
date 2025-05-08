import math


class Solution:

    def isPrime(self, num: int) -> bool:

        if num < 2:
            return False

        if num == 2 or num == 3:
            return True

        if num % 2 == 0 or num % 3 == 0:
            return False

        for i in range(5, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False

        return True

    def maximumPrimeDifference(self, nums: list[int]) -> int:

        primeIndices = [i for i, val in enumerate(nums) if self.isPrime(val)]

        if len(primeIndices) < 2:
            return 0

        return primeIndices[-1] - primeIndices[0]


newMax = Solution()
print(newMax.maximumPrimeDifference([1, 2, 3, 4, 5]))
