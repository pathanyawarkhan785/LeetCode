class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        print(items, ruleKey, ruleValue)


newCount = Solution()
newCount.countMatches(
    [
        ["phone", "blue", "pixel"],
        ["computer", "silver", "lenovo"],
        ["phone", "gold", "iphone"],
    ],
    "color",
    "silver",
)
