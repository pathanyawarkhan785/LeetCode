class Solution:
    def interpret(self, command):
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command


newInterpret = Solution()
print(newInterpret.interpret("G()(al)"))
