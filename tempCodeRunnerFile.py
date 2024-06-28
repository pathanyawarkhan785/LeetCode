class Solution:
    def largestOddNumber(self, num):

        if int(num) % 2:
            return num

        for i in reversed(range(len(num))):
            if int(num[i]) % 2 == 0:
                num = num.replace(num[i], "#")

        if len(num) <= 0:
            return ""