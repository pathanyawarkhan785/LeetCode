class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append([t, i])

        return res


newDaily = Solution()
print(newDaily.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
