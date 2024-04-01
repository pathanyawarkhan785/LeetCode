class Solution:
    def mostWordsFound(self, sentences):
        num = [len(sentences[i].split(" ")) for i in range(len(sentences))]
        return max(num)


newMostWords = Solution()
print(
    newMostWords.mostWordsFound(
        [
            "alice and bob love leetcode",
            "i think so too",
            "this is great thanks very much",
        ]
    )
)
