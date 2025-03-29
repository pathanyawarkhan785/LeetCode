class Solution:
    def removeStars(self, s):
        stack = []

        for val in s:

            if val == "*":
                stack and stack.pop()
            else:
                stack.append(val)

        return "".join(stack)


newRemove = Solution()
print(newRemove.removeStars("leet**cod*e"))
