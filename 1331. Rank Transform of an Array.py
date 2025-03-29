class Solution:
    def arrayRankTransform(self, arr):

        # method 1

        sortedUniqueArr = sorted(set(arr))
        indValPair = {ele: rank + 1 for rank, ele in enumerate(sortedUniqueArr)}
        ranked_arr = [indValPair[ele] for ele in arr]
        return ranked_arr

        # method 2

        # return (
        #     [rank[x] for x in arr]
        #     if (rank := {x: i + 1 for i, x in enumerate(sorted(set(arr)))})
        #     else []
        # )


newArray = Solution()
print(newArray.arrayRankTransform([40, 10, 30, 20, 30]))
