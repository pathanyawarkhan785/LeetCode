class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for val in hours:
            if val >= target:
                count += 1
        return count


newNumberOfEmployee = Solution()
print(newNumberOfEmployee.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2))
