class Solution:
    def generateTheString(self, n: int) -> str:
        lst = ["y"]

        if len(lst) == n:
            return lst

        while len(lst) + 1 < n:
            lst.append("y")
            lst.append("y")
            if len(lst) == n:
                return lst

        lst.append("w")
        return lst


newGenerate = Solution()
print(newGenerate.generateTheString(3))
