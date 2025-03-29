class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        from collections import defaultdict

        groups = defaultdict(list)
        result = []

        for idx, size in enumerate(groupSizes):
            groups[size].append(idx)
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result


newGroup = Solution()
print(newGroup.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
