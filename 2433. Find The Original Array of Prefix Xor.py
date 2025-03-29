class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        arr = [0] * n
        arr[0] = pref[0]

        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]

        return arr


newFind = Solution()
print(newFind.findArray([5, 2, 0, 3, 1]))
