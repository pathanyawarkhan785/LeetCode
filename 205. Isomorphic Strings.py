# class Solution:
#     def isIsomorphic(self, s, t):
#         temp = ""
#         for i in s:
#             if i not in temp:
#                 temp += i
#         print(temp)


# newIsIsomorphic = Solution()
# newIsIsomorphic.isIsomorphic("egg", "add")

foo = "mppmt"
result = "".join(dict.fromkeys(foo))
print(result)
