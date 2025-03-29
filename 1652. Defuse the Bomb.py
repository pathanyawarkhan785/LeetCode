class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        temp = 2 * code
        n = len(code)
        if k == 0:
            return n * [0]
        elif k > 0:
            return [sum(temp[i + 1 : i + 1 + k]) for i in range(n)]
        else:
            return [sum(temp[n + i + k : n + i]) for i in range(n)]


newDecrypt = Solution()
print(newDecrypt.decrypt([5, 7, 1, 4], 3))
