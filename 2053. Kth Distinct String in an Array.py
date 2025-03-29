class Solution:
    def kthDistinct(self, arr, k):

        count = {}
        for item in arr:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1

        distinct = [item for item in arr if count[item] == 1]

        if len(distinct) >= k:
            return distinct[k - 1]
        return ""


newKth = Solution()
print(newKth.kthDistinct(["a", "b", "a"], 3))
