class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing white spaces
        if not s:
            return 0

        i, sign, num = 0, 1, 0

        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num


newMyAtoi = Solution()
print(newMyAtoi.myAtoi("   -42"))
