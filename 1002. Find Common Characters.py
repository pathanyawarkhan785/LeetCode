class Solution:
    def commonChars(self, words):
        words.sort(key=len)
        # print(words)
        for i in range(len(words)):
            # print(i, words[i])
            for j in range(len(words[i])):
                if (
                    (words[i][j] in words[j + 1])
                    and (j < 2)
                    and words[i][j] in words[j + 2]
                ):
                    print(words[i][j])
                    break


newCommonChars = Solution()
newCommonChars.commonChars(["bella", "label", "roller"])
