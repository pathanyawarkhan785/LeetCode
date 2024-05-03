class Solution:
    def gcdOfStrings(self, str1, str2):
        for i in range(len(str2)):
            if str1[i] == str2[i]:
                str1 = str1.replace(str1[i], " ", 1)
            else:
                return ""
        str1.replace(" ", "")
        print(str1, str2)
        return str1.replace(" ", "")


newGcdOfStrings = Solution()
print(newGcdOfStrings.gcdOfStrings("ABABAB", "ABAB"))
