class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = set(sentence)
        return len(pangram) == 26


newCheck = Solution()
print(newCheck.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
