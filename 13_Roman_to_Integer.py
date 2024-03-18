class Solution:
    def romanToInt(self, val):

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0

        for i in range(len(val)):
            if i + 1 < len(val) and roman[val[i]] < roman[val[i + 1]]:
                res -= roman[val[i]]
            else:
                res += roman[val[i]]

        return res


newRomanToInt = Solution()
print(newRomanToInt.romanToInt("III"))
