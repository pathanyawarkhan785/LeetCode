class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # arr = ["This    is    an", "example  of text", "justification.  "]

        for i in range(len(words)):
            print(len(words[i]), maxWidth)


newFull = Solution()
newFull.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
