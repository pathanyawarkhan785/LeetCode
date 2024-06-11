class Solution:
    def findRelativeRanks(self, score):
        temp = score.copy()
        print(temp)
        while len(score) != 0:
            maxInd = score.index(max(score))
            print(f"score : {score}")
            print(f"maxInd : {maxInd}")
            if "Gold Medal" not in temp:
                temp[maxInd] = "Gold Medal"
                score.remove(max(score))
                # print(score)
            elif "Silver Medal" not in temp:
                temp[maxInd] = "Siver Medal"
                score.remove(max(score))
                print(temp)
                break


newFindRelativeRanks = Solution()
newFindRelativeRanks.findRelativeRanks([10, 3, 8, 9, 4])
