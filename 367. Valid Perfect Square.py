class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num < 2:
            return True

        start = 2
        end = num // 2

        while start <= end:
            mid = (start + end) // 2
            sq = mid**2

            if sq < num:
                start = mid + 1

            elif sq > num:
                end = mid - 1

            else:
                return True

        return False


newPerfect = Solution()
print(newPerfect.isPerfectSquare(104976))
