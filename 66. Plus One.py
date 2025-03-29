lst = [1, 2, 3]


class Solution:
    def plusOne(self, lst):
        num = int("".join(map(str, lst))) + 1
        return [int(digit) for digit in str(num)]


newPlusOne = Solution()
print(newPlusOne.plusOne(lst))
