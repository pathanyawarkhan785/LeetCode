class Solution:
    def fizzBuzz(self, n):
        newList = []
        for val in range(1, n + 1):
            if val % 3 == 0 and val % 5 == 0:
                newList.append("FizzBuzz")
            elif val % 3 == 0:
                newList.append("Fizz")
            elif val % 5 == 0:
                newList.append("Buzz")
            else:
                newList.append(str(val))
        return newList


newFizzBuzz = Solution()
print(newFizzBuzz.fizzBuzz(3))
