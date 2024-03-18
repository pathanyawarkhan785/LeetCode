class Solution:
    def largestOddNumber(self, num):
        if int(num) % 2 == 0:
            num = int(num) / 10
        print(num)


newLargest = Solution()
print(newLargest.largestOddNumber("4206"))
