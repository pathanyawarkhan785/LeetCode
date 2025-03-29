from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)

        steps = 0

        for char, count in s.items():
            if char in t:
                steps += max(0, count - t[char])
            else:
                steps += count

        return steps


newMinSteps = Solution()
print(newMinSteps.minSteps("bab", "aba"))
