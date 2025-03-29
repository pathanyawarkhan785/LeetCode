class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s not in s_to_t:
                s_to_t[char_s] = char_t
            if char_t not in t_to_s:
                t_to_s[char_t] = char_s

            if s_to_t[char_s] != char_t or t_to_s[char_t] != char_s:
                return False

        return True


newIsIsomorphic = Solution()
print(newIsIsomorphic.isIsomorphic("paper", "title"))

# foo = "mppmt"
# result = "".join(dict.fromkeys(foo))
# print(result)
