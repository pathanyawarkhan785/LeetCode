class Solution:
    def strStr(self, haystack, needle):

        return haystack.index(needle) if needle in haystack else -1


occurFirst = Solution()
print(occurFirst.strStr("sadbutsad", "sad"))
