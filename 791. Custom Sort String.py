from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:

        hashMap = Counter(s)
        temp = ""

        for i in order:
            temp += i * hashMap[i]
            s = s.replace(i, "")
        return temp + s


newCustom = Solution()
print(newCustom.customSortString("kqep", "pekeq"))
