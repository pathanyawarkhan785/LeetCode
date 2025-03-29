class Solution:
    def countTestedDevices(self, batteryPercentages):

        # print(batteryPercentages)

        testedDevice = 0

        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                testedDevice += 1

                for j in range(i + 1, len(batteryPercentages)):
                    if batteryPercentages[j] <= 0:
                        batteryPercentages[j] = 0
                    batteryPercentages[j] = batteryPercentages[j] - 1

            # print(batteryPercentages)

        # print(batteryPercentages[i])
        return testedDevice


newCount = Solution()
print(newCount.countTestedDevices([1, 1, 2, 1, 3]))
