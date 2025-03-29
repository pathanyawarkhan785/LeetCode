class Solution:
    def removeAnagrams(self, words):
        newWords = []
        for word in words:
            word = "".join(sorted(word))
            print(word)
            # if word in words:
            # words.remove(word)
            # print(words)


newRemove = Solution()
newRemove.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"])
