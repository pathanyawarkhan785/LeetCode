# class Solution:
#     def findSubstringInWraproundString(self, s):
#         print(s)


# newFindSubstring = Solution()
# newFindSubstring.findSubstringInWraproundString("zab")


def subsequences(string):
    memo = {}

    def helper(s):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        first = s[0]
        rest_subseq = helper(s[1:])
        result = rest_subseq + [first + subseq for subseq in rest_subseq]
        memo[s] = result
        return result

    return helper(string)
