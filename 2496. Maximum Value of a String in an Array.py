class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        maxVal = 0

        for s in strs:
            if s.isnumeric():
                val = int(s)
            else:
                val = len(s)

            if val > maxVal:
                maxVal = val

        return maxVal


newMaximum = Solution()
print(newMaximum.maximumValue(["alic3", "bob", "3", "4", "00000"]))
