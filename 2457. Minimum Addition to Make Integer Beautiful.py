class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        current_sum = lambda x: sum(int(d) for d in str(x))
        add = 0
        current = n

        while current_sum(current) > target:
            digits = list(str(current))
            carry_index = len(digits) - 1

            while carry_index >= 0:
                if digits[carry_index] != "0":
                    break
                carry_index -= 1

            add += 10 ** (len(digits) - carry_index - 1)
            current += 10 ** (len(digits) - carry_index - 1)

        return add


newBeautiful = Solution()
print(newBeautiful.makeIntegerBeautiful(165, 10))
