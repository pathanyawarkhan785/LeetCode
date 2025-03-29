class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:

        count = 0

        for st in words:
            if st.startswith(pref):
                count += 1

        return count


newPrefix = Solution()
print(newPrefix.prefixCount(["pay", "attention", "practice", "attend"], "at"))
