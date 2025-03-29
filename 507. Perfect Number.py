class Solution(object):
    def checkPerfectNumber(self, num):

        if num <= 1:
            return False

        sum = 1

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                sum += i
                if i != num // i:
                    sum += num // i
        return sum == num


newPerfect = Solution()
print(newPerfect.checkPerfectNumber(28))
