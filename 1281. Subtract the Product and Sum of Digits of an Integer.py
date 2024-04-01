class Solution:
    def subtractProductAndSum(self, n):
        product = 1
        sum = 0
        n = str(n)
        for i in range(len(n)):
            product *= int(n[i])
            sum += int(n[i])

        return product - sum


newSubtractProduct = Solution()
print(newSubtractProduct.subtractProductAndSum(234))
