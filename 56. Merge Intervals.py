class Solution:
    def merge(self, intervals):
        intervals.sort()
        newIntervals = []
        elem1 = 1
        elem2 = 0
        i = 0
        while i + 1 < len(intervals) and intervals[i][elem1] > intervals[i + 1][elem2]:
            if (
                i + 1 < len(intervals)
                and intervals[i][elem1] >= intervals[i + 1][elem2]
            ):
                if intervals[i][elem1] > intervals[i + 1][elem1]:
                    newIntervals.append(intervals[i])
                else:
                    newIntervals.append([intervals[i][elem2], intervals[i + 1][elem1]])
                del intervals[i : i + 2]
            i = i + 1

        newIntervals += intervals
        newIntervals.sort()
        return newIntervals


newMerge = Solution()
print(newMerge.merge([[1, 4], [0, 2], [3, 5]]))
