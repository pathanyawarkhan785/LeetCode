class Solution:

    def climbStairs(self, n):
        first = 0
        second = 1

        if n < 1:
            raise "kindly enter correct number !"
        elif n == 1 or n == 2:
            return n
        else:
            for i in range(0, n):
                res = first + second
                first = second
                second = res
            return res


newClimbStairs = Solution()
print(newClimbStairs.climbStairs(5))
