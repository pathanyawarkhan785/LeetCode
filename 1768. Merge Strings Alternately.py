class Solution:
    def mergeAlternately(self, word1, word2):
        minStr = min(len(word1), len(word2))
        temp = ""
        for i in range(0, minStr):
            temp += word1[i] + word2[i]

        if len(word1) == len(word2):
            return temp
        elif len(word1) < len(word2):
            return temp + word2[minStr:]
        else:
            return temp + word1[minStr:]

        return temp


newMergeAlternately = Solution()
print(newMergeAlternately.mergeAlternately("abcd", "pq"))
