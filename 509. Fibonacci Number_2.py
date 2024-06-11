class Solution:
    def fib(self, n):
        temp = [0, 1]
        for i in range(2, n + 1):
            temp.append(temp[i - 1] + temp[i - 2])
        return temp[n]


newFib = Solution()
print(newFib.fib(10))
