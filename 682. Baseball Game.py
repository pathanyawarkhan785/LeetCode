class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op.lstrip("-").isdigit():
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
        return sum(stack)


newCal = Solution()
print(newCal.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
