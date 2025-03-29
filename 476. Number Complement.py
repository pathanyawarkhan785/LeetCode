class Solution:
    def findComplement(self, num: int) -> int:

        # method 1

        # binNum = bin(num)[2:]

        # binNum = binNum.replace("1", "#")
        # binNum = binNum.replace("0", "1")
        # binNum = binNum.replace("#", "0")

        # return int(binNum, 2)

        # method 2 using bit manpulation

        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1
        return num ^ mask


newFind = Solution()
print(newFind.findComplement(5))
