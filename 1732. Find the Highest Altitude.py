class Solution:
    def largestAltitude(self, gain):

        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]

        if max(gain) < 1:
            return 0

        return max(gain)


newLargest = Solution()
print(newLargest.largestAltitude([-5, 1, 5, 0, -7]))
