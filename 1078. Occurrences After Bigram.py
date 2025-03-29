class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        result = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])

        return result


newFind = Solution()
print(newFind.findOcurrences("alice is a good girl she is a good student", "a", "good"))
