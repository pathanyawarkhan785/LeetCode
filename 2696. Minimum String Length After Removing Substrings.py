# class Solution:
#     def minLength(self, s):

#         # method 1

#         while "AB" or "CD" in s:

#             if "AB" not in s and "CD" not in s:
#                 return len(s)

#             if "AB" in s:
#                 s = s.replace("AB", "")

#             elif "CD" in s:
#                 s = s.replace("CD", "")

#         return len(s)

# using stack


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for val in s:
            if not stack:
                stack.append(val)
            else:
                if stack[-1] == "A" and val == "B":
                    stack.pop()
                elif stack[-1] == "C" and val == "D":
                    stack.pop()
                else:
                    stack.append(val)

        return len(stack)


newMinLength = Solution()
print(newMinLength.minLength("ABFCACDB"))
