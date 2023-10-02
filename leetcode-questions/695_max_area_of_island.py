from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max = 0

        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c)
                    if area > max:
                        max = area

        return max

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
            return 0

        area = 1
        grid[row][col] = 0

        area += self.dfs(grid, row - 1, col)
        area += self.dfs(grid, row + 1, col)
        area += self.dfs(grid, row, col - 1)
        area += self.dfs(grid, row, col + 1)

        return area
