import math


class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        if n in [2, 3, 5]:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def findPrimePairs(self, n: int) -> list[list[int]]:
        if n < 2:
            return []

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        result = []
        for x in range(2, n // 2 + 1):
            y = n - x
            if y >= x and is_prime[x] and is_prime[y]:
                result.append([x, y])

        return result


newPrime = Solution()
print(newPrime.findPrimePairs(10))
