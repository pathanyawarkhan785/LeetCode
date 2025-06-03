from collections import defaultdict


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        from collections import defaultdict

        freq = defaultdict(int)
        for char in s:
            freq[char] += 1

        for _ in range(t):
            new_freq = defaultdict(int)
            new_length = 0
            for char, count in freq.items():
                if char == "z":
                    new_freq["a"] += count
                    new_freq["b"] += count
                    new_length += 2 * count
                else:
                    next_char = chr(ord(char) + 1)
                    new_freq[next_char] += count
                    new_length += count
            freq = new_freq
            length = new_length % MOD

        return length


newTransformation = Solution()
print(newTransformation.lengthAfterTransformations("abcyy", 2))
