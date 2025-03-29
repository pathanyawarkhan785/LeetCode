# class Solution:
#     def isPowerOfTwo(self, n):
#         if n == 1:
#             return True
#         while n > 1:
#             if n == 2:
#                 return True
#             elif n % 2 == 0:
#                 n = n / 2
#             else:
#                 return False


class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        return n & (n - 1) == 0


newIsPowerOfTwo = Solution()
print(newIsPowerOfTwo.isPowerOfTwo(16))
