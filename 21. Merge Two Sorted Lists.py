class Solution:
    def mergeTwoLists(self, list1, list2):
        list1.extend(list2)
        list1.sort()
        return list1


newMergeList = Solution()
print(newMergeList.mergeTwoLists([1, 2, 4], [1, 3, 4]))
