class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        start = 0
        end = int(c**0.5)

        while start <= end:
            currSum = start**2 + end**2
            if currSum > c:
                end -= 1
            elif currSum < c:
                start += 1
            else:
                return True

        return False


newJudge = Solution()
print(newJudge.judgeSquareSum(2))
