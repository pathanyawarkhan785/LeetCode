from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        count = Counter(digits)
        result = set()

        for h in range(1, 10):
            for t in range(10):
                for u in range(0, 10, 2):
                    num = [h, t, u]
                    temp_count = Counter(num)

                    if all(temp_count[d] <= count[d] for d in temp_count):
                        result.add(h * 100 + t * 10 + u)

        return sorted(result)


newFind = Solution()
print(newFind.findEvenNumbers([2, 2, 8, 8, 2]))
