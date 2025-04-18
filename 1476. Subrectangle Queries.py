class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


newSub = SubrectangleQueries()
newSub.getValue(
    [
        [[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]],
        [0, 2],
        [0, 0, 3, 2, 5],
        [0, 2],
        [3, 1],
        [3, 0, 3, 2, 10],
        [3, 1],
        [0, 2],
    ]
)
