class Solution:
    def largestOddNumber(self, num):

        if int(num) % 2:
            return num

        numLen = len(num) - 1
        print(numLen, num[numLen])

        while 1:
            if int(num[numLen]) % 2 == 0:
                num = num.replace(num[numLen], " ")
                numLen = numLen - 1

        print(num)

        # for val in reversed(num):
        #     if int(val) % 2 == 0:
        #         num = num.replace(val, " ")

        if len(num) <= 0:
            return ""

        return num


newLargest = Solution()
print(newLargest.largestOddNumber("4206"))
