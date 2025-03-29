class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        result = 0
        for char in s + t:
            result ^= ord(char)
            print(result)
        return chr(result)


newFindDifference = Solution()
print(newFindDifference.findTheDifference("a", "aa"))
