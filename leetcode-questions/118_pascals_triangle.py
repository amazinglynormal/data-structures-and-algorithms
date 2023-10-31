from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        row = 0

        while row < numRows:
            if row == 0:
                result.append([1])

            elif row == 1:
                result.append([1, 1])

            else:
                temp = []
                for i in range(row + 1):
                    if i == 0 or i == row:
                        temp.append(1)
                    else:
                        temp.append(result[row - 1][i - 1] + result[row - 1][i])
                result.append(temp)

            row += 1

        return result
