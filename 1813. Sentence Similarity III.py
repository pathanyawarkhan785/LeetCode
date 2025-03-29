class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        i, j = 0, 0

        while (
            i < len(sentence1) and i < len(sentence2) and sentence1[i] == sentence2[i]
        ):
            i += 1
        while (
            j < len(sentence1) - i
            and j < len(sentence2) - i
            and sentence1[~j] == sentence2[~j]
        ):
            j += 1
        return i + j == min(len(sentence1), len(sentence2))


newAre = Solution()
print(newAre.areSentencesSimilar("My name is Haley", "My Haley"))
