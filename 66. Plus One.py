lst = [1, 2, 3]


class Solution:
    def plusOne(self, lst):
        temp = ""

        for val in lst:
            temp += str(val)

        temp = int(temp)
        temp = temp + 1
        temp = str(temp)

        lst = []

        for val in temp:
            lst.append(int(val))

        return lst


newPlusOne = Solution()
print(newPlusOne.plusOne(lst))
