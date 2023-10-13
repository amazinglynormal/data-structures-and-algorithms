from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        prev_row = [0] * COLS

        for row in range(ROWS - 1, -1, -1):
            curr_row = [0] * COLS
            for col in range(COLS - 1, -1, -1):
                if row == ROWS - 1 and col == COLS - 1 and obstacleGrid[row][col] != 1:
                    curr_row[-1] = 1
                elif obstacleGrid[row][col] == 1:
                    curr_row[col] = 0
                else:
                    if col < COLS - 1:
                        curr_row[col] = prev_row[col] + curr_row[col + 1]
                    else:
                        curr_row[col] = prev_row[col]
            prev_row = curr_row

        return prev_row[0]


sol = Solution()
sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
