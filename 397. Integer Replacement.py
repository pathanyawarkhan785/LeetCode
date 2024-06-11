class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while 1:
            if n == 1:
                return count
            if n % 2 == 0:
                n = n // 2
                count = count + 1
                print(f"{n} -> {count}")
            else:
                n = n - 1
                count = count + 1
                print(f"{n} -> {count}")

        # print(count)


newIntegerReplacement = Solution()
print(newIntegerReplacement.integerReplacement(7))
