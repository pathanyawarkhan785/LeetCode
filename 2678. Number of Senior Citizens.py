class Solution:
    def countSeniors(self, details):
        count = 0
        for i in range(len(details)):
            if int(details[i][11:13]) > 60:
                count += 1
        return count


newCount = Solution()
print(newCount.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
