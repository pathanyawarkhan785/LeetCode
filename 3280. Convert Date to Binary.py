class Solution:
    def convertDateToBinary(self, date: str) -> str:

        return (
            bin(int(date[:4]))[2:]
            + "-"
            + bin(int(date[5:7]))[2:]
            + "-"
            + bin(int(date[8:]))[2:]
        )


newConvert = Solution()
print(newConvert.convertDateToBinary("2080-02-29"))
