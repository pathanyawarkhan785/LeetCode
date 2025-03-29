class Solution:
    def lemonadeChange(self, bills):

        five = ten = 0

        for bill in bills:

            if bill == 5:
                five += 1

            elif bill == 10:
                ten += 1

            change = bill - 5

            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False

            elif change == 15:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True


newLemonade = Solution()
print(newLemonade.lemonadeChange([5, 10]))
