class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in range(0, len(operations)):
            if "-" in operations[i]:
                x -= 1
            else:
                x += 1
        return x


newFinalValue = Solution()
print(newFinalValue.finalValueAfterOperations(["--X", "X++", "X++"]))
