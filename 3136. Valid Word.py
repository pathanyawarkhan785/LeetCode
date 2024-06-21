# class Solution:
#     def isValid(self, word):

#         if len(word) < 3:
#             return False

#         word = word.lower()

#         vowels = "aeiou"
#         consonants = "qwertyuiopasdfghjklzxcvbnm"

#         has_vowel = False
#         has_consonant = False

#         res = vowels + consonants + "1234567890"

#         for c in word:
#             if c in vowels:
#                 has_vowel = True
#             if c in consonants:
#                 has_consonant = True
#             if c not in res:
#                 return False

#         return has_vowel and has_consonant


# newIsValid = Solution()
# print(newIsValid.isValid("234Adas"))
