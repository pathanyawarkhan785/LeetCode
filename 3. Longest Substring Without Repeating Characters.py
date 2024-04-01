class Solution:
    def lengthOfLongestSubstring(self, s):
        # lst = [s[i] for i in range(len(s))]
        for ind, val in enumerate(s):
            # print(ind, val)
            if s.count(val) > 1:
                print(s.index(val))
                # return

        # print(lst)x


newSubString = Solution()
newSubString.lengthOfLongestSubstring("abcabcbb")
