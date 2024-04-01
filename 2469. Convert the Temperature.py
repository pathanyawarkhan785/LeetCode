class Solution:
    def convertTemperature(self, celsius):
        return [(celsius + 273.15), (celsius * 1.80 + 32.00)]


newConvert = Solution()
print(newConvert.convertTemperature(36.5))
