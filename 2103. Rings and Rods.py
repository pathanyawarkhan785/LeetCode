class Solution:
    def countPoints(self, rings: str) -> int:
        allRods = {str(i): set() for i in range(10)}

        for i in range(0, len(rings), 2):
            colours = rings[i]
            oneRode = rings[i + 1]
            # print(oneRode)
            allRods[oneRode].add(colours)
            # return allRods
        # return allRods

        count = 0
        for rod in allRods.values():
            # print(rod)
            if len(rod) == 3:
                count += 1
        # print(count)
        # print(allRods)

        return count


newCount = Solution()
print(newCount.countPoints("R3G2B1R0G0B0"))
