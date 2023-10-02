from typing import List


def dfs(grid: List[List[str]], row: int, col: int):
    ROWS = len(grid)
    COLS = len(grid[0])

    if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
        return

    grid[row][col] = "0"
    # up
    dfs(grid, row - 1, col)
    # down
    dfs(grid, row + 1, col)
    # left
    dfs(grid, row, col - 1)
    # right
    dfs(grid, row, col + 1)


def numIslands(grid: List[List[str]]) -> int:
    num_of_islands = 0

    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if grid[r][c] == "1":
                num_of_islands += 1
                dfs(grid, r, c)

    return num_of_islands
