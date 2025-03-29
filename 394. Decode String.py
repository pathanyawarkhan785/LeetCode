class Solution:
    def decodeString(self, s):
        stack = []
        newStr = ""

        for i in range(len(s)):

            if s[i] != "]":
                stack.append(s[i])
            else:
                newStr = ""
                while stack[-1] != "[":
                    newStr = stack.pop() + newStr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * newStr)

        return "".join(stack)


newDecode = Solution()
print(newDecode.decodeString("3[a]2[bc]"))
