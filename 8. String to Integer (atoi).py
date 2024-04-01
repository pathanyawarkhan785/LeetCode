class Solution:
    def myAtoi(self, s):
        temp = ""
        for i in range(0, len(s)):
            if s[i].isalpha():
                return ""
            elif s[i].isdigit() or s[i] == "-":
                temp += s[i]
            elif s[i] == " ":
                if len(temp) > 0:
                    return int(temp)
                return temp

        return int(temp)


newMyAtoi = Solution()
print(newMyAtoi.myAtoi("   -42"))
