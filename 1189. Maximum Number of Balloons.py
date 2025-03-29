from collections import Counter

# method 1


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = 0

        if len(text) < 7:
            return 0

        chars_to_count = "balon"

        text = "".join([ch for ch in text if ch in chars_to_count])
        text = Counter(text)

        while (
            text["b"] >= 1
            and text["a"] >= 1
            and text["l"] >= 2
            and text["o"] >= 2
            and text["n"] >= 1
        ):

            count += 1
            text["b"] -= 1
            text["a"] -= 1
            text["l"] -= 2
            text["o"] -= 2
            text["n"] -= 1

        return count


# method 2


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = Counter(text)
        return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])


# balloon
# b -> 1
# a -> 1
# l -> 2
# o -> 2
# n -> 1


newMax = Solution()
print(
    newMax.maxNumberOfBalloons(
        "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    )
)
