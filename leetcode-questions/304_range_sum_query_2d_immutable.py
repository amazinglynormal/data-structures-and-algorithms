from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sumMatrix = self.__build_sum_matrix(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = self.sumMatrix[row2][col2]
        if row1 > 0:
            totalSum -= self.sumMatrix[row1 - 1][col2]
        if col1 > 0:
            totalSum -= self.sumMatrix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            totalSum += self.sumMatrix[row1 - 1][col1 - 1]

        return totalSum

    def __build_sum_matrix(self, matrix: List[List[int]]) -> List[List[int]]:
        sumMatrix = []
        for i in range(len(matrix)):
            row = []
            rowSum = 0
            for j in range(len(matrix[i])):
                rowSum += matrix[i][j]
                prevRow = sumMatrix[i - 1][j] if i > 0 else 0
                row.append(rowSum + prevRow)
            sumMatrix.append(row)

        return sumMatrix
