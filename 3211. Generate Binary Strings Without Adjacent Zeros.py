class Solution:
    def validStrings(self, n: int) -> list[str]:
        result = []
        stack = [""]

        while stack:
            current = stack.pop()
            if len(current) == n:
                result.append(current)
            else:
                stack.append(current + "1")
                if not current or current[-1] != "0":
                    stack.append(current + "0")

        return result


newValid = Solution()
print(newValid.validStrings(3))
