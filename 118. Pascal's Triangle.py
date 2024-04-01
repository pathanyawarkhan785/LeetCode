class Solution:
    def generate(self, numRows):
        temp = []

        for i in range(1, numRows + 1):
            if i > 2:
                for j in range(0, len(temp)):
                    # center = int(len(temp) / 2)
                    # temp.insert(center, temp[j] + temp[j + 1])
                    # return temp
                    

            temp.append(1)
            print(temp)


newGenerate = Solution()
print(newGenerate.generate(3))
