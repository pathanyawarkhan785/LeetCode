class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        temp = 0
        for i in range(len(seats)):
            temp += abs(seats[i] - students[i])
        return temp


newMinToSeat = Solution()
print(newMinToSeat.minMovesToSeat([3, 1, 5], [2, 7, 4]))
