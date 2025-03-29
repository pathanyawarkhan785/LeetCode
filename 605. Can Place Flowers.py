class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        # print(flowerbed)

        for i in range(1, len(flowerbed) - 1):
            # print(flowerbed[i])
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0


newCanPlace = Solution()
print(newCanPlace.canPlaceFlowers([1, 0, 0, 0, 1], 2))
