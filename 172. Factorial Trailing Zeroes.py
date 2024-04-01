class Solution:
    def trailingZeroes(self, n):
        factorial = 1
        if n < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif n == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1, n + 1):
                factorial = factorial * i

        count = 0

        while factorial % 10 == 0:
            count += 1
            factorial = factorial // 10
        return count


newTrailing = Solution()
print(newTrailing.trailingZeroes(30))
