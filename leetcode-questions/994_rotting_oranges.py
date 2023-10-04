from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up,down,left,right
        queue = deque()
        fresh = 0
        longest_minutes = 0

        for row, grid_row in enumerate(grid):
            for col, _ in enumerate(grid_row):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        mins = -1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc
                    if (
                        min(newRow, newCol) < 0  # out of bounds
                        or newRow >= ROWS  # out of bounds
                        or newCol >= COLS  # out of bounds
                        or grid[newRow][newCol] == 0  # cell empty
                        or grid[newRow][newCol] == 2  # already rotten
                    ):
                        continue
                    grid[newRow][newCol] = 2
                    fresh -= 1
                    queue.append((newRow, newCol))
            mins += 1

        if mins > longest_minutes:
            longest_minutes = mins

        if fresh > 0:
            return -1

        return longest_minutes


sol = Solution()

case1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
case2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
case3 = [[0, 2]]
case4 = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]

print(sol.orangesRotting(case1))  # 4
print(sol.orangesRotting(case2))  # -1
print(sol.orangesRotting(case3))  # 0
print(sol.orangesRotting(case4))  # 2
