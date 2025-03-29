class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # print(len(str1))
        # print(len(str2))

        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) == len(str2):
            return str1

        # print((str1, str2[len(str1) :]))
        # print(len(str1), len(str2[len(str1) :]))

        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2) :], str2)
        return self.gcdOfStrings(str1, str2[len(str1) :])


newGcdOfStrings = Solution()
print(newGcdOfStrings.gcdOfStrings("ABCABC", "ABC"))
