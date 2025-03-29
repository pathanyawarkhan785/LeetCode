class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        lenOfSkill = len(skill)
        if lenOfSkill % 2 == 1:
            return -1

        skill.sort()
        left, right = 0, lenOfSkill - 1
        total = 0
        target_sum = sum(skill) // (lenOfSkill // 2)

        while left < right:
            current_sum = skill[left] + skill[right]
            if current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                return -1
            else:
                total += skill[left] * skill[right]
                left += 1
                right -= 1

        return total


newDivide = Solution()
print(newDivide.dividePlayers([10, 14, 16, 15, 9, 4, 4, 4]))
