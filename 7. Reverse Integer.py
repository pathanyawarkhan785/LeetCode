class Solution:
    def reverse(self, x):
        temp = x
        temp = str(temp)
        if int(temp) < 0:
            temp = temp.replace(temp[0], "")
            temp = temp[::-1]
            temp = -int(temp)
            if temp < -2147483648:
                return 0
            return temp

        temp = temp[::-1]
        temp = int(temp)
        if temp > 2147483647:
            return 0

        return temp


newReverse = Solution()
print(newReverse.reverse(-23))
