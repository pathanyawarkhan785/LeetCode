class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1

        while factor <= n:
            leftPart = n // (factor * 10)
            currDigit = (n // factor) % 10
            rightPart = n % factor

            print(rightPart)

            if currDigit == 0:
                count += leftPart * factor
            elif currDigit == 1:
                count += leftPart * factor + rightPart + 1
            else:
                count += (leftPart + 1) * factor

            factor *= 10

        return count


newCount = Solution()
print(newCount.countDigitOne(1234))
