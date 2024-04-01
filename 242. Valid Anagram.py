class Solution:
    def isAnagram(self, s, t):
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return True if (s == t) else False


newIsAnagram = Solution()
print(newIsAnagram.isAnagram("anagram", "nagaram"))
# import counter class from collections module
from collections import Counter

# Creation of a Counter Class object using
# string as an iterable data container
x = Counter("geeksforgeeks")

# printing the elements of counter object
for i in x.elements():
    print(i, end=" ")
