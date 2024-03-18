class Solution:
    def isValid(self, s):
        myPare = []

        for c in s:
            if c == "(":
                myPare.append(")")
            elif c == "{":
                myPare.append("}")
            elif c == "[":
                myPare.append("]")
            elif not myPare or myPare.pop() != c:
                return False

        return not myPare


newVaild = Solution()
print(newVaild.isValid("(){}"))
