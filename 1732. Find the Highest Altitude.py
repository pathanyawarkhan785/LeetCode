class Solution:
    def largestAltitude(self, gain):

        gain = [0] + gain

        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]

        return max(gain)


newLargest = Solution()
print(newLargest.largestAltitude([-5, 1, 5, 0, -7]))
