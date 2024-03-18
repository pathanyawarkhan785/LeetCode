class Solution:
    def fib(self, n):
        first = 0
        second = 1
        count = 0
        if n <= 0:
            return first

        elif n == 1:
            return second

        else:
            while count < n - 1:
                temp = first + second
                first = second
                second = temp
                count += 1
            return temp


newFib = Solution()
print(newFib.fib(4))


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
