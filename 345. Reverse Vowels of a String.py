class Solution:
    def reverseVowels(self, s):
        vowelsList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        start = 0
        end = len(s) - 1
        s = list(s)

        while start < end:

            if s[start] not in vowelsList:
                start += 1
            elif s[end] not in vowelsList:
                end -= 1
            else:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        s = "".join(s)

        # print(s[start], s[end])
        # print(s)

        return s


# print(s[i])


newReverseVowels = Solution()
print(newReverseVowels.reverseVowels("IceCreAm"))
