class Solution:
    def mySqrt(self, x):

        if x < 2:
            return x

        start = 1
        end = x

        while start <= end:
            mid = (end + start) // 2
            sq = mid * mid

            if sq == x:
                return mid

            elif sq < x:
                start = mid + 1

            else:
                end = mid - 1

        return end


newMySqrt = Solution()
print(newMySqrt.mySqrt(8))
