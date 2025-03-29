class Solution:
    def destCity(self, paths: list[list[str]]) -> str:

        # method 1

        hashMap = set()

        for i in range(len(paths)):
            hashMap.add(paths[i][0])

        for i in range(len(paths)):
            if paths[i][1] not in hashMap:
                return paths[i][1]

        # method 2

        starting_cities = {path[0] for path in paths}
        for path in paths:
            if path[1] not in starting_cities:
                return path[1]


newDest = Solution()
print(newDest.destCity([["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]))
