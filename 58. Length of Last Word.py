s = "luffy is still     joyboy          "


class Solution:
    def lengthOfLastWord(self, s):

        # try 1
        # s = s.split(" ")
        # return len(s[len(s) - 1])

        # try 2
        # s = s.replace(" ", "")
        # print(s)
        # print(len(s))

        # try 3
        s = s.strip()
        s = s.split(" ")
        print(len(s[-1]))


# newLen = Solution()
# print(newLen.lengthOfLastWord(s))
