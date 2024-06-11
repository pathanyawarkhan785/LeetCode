class Solution:
    def relativeSortArray(self, arr1, arr2):
        temp = []
        newArr1 = []
        for i in range(len(arr2)):
            temp.append([arr2[i]] * arr1.count(arr2[i]))
            # newArr1.remove(arr2[i])
        temp = sum(temp, [])
        for i in range(len(arr1)):
            if arr1[i] not in temp:
                newArr1.append(arr1[i])

        newArr1.sort()
        temp.extend(newArr1)
        return temp


newRelative = Solution()
print(
    newRelative.relativeSortArray(
        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
    )
)
