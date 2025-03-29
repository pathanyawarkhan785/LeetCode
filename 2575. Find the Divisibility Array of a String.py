class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        res = [0] * len(word)
        currNum = 0

        for i in range(len(word)):
            currNum = currNum * 10 + int(word[i])
            if currNum % m == 0:
                res[i] = 1
            currNum %= m

        return res


newDivisible = Solution()
print(newDivisible.divisibilityArray("998244353", 3))
